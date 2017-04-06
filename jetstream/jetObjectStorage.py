import configuration.globalVars as globalVars
import jetAuth as jetAuth
import requests
import json
import os
import Queue
import threading

class BufferQueue(Queue.Queue):
   
   def __iter__(self):
      return iter(self.get, None)

   def close(self):
      self.put(None)

# Sends the data to Swift from the buffer (consumer)
def send_data(data, url, my_headers):
   r = requests.put(url, data=data, headers=my_headers)

# Takes the data from the camera and put it in the buffer (producer)
def fill_queue(data, queue, chunkSize):
   
   bytecount = 0
      
   #Loop until the chunkSize amount of bytes have been put into the buffer
   while bytecount < chunkSize:
      amount = min(1000, chunkSize, (chunkSize - bytecount))
      queue.put(data.read(amount))
      bytecount += amount
						         
   #Close the buffer so that the consumer knows there is no more data
   queue.close()

def putObject(fileName, path, objectData):
    url = globalVars.jetstreamObjectStorageURL + "/" + globalVars.jetstreamContainerName + path + fileName

    counter = 1
    fileByteCount = 0
    oldPosition = objectData.tell()
    objectData.seek(0, os.SEEK_END)
    fileTotalCount = objectData.tell()
    objectData.seek(oldPosition, os.SEEK_SET)

    while fileByteCount < fileTotalCount:

       token_id = jetAuth.auth()
       my_headers = {"Content-Type": 'binary/octet-stream', "Transfer-Encoding": "chunked", "X-Auth-Token": token_id}

       # Create a new buffer for streaming
       q = BufferQueue(globalVars.bufferSize)

       # Setup the file extension if multiple parts are required
       if fileTotalCount > globalVars.uploadSize:
          extension = "." + str(counter)
	  counter = counter + 1
       else:
          extension = ""

       consumer = threading.Thread(target=send_data, args=(q, url+extension, my_headers,))
       producer = threading.Thread(target=fill_queue, args=(objectData, q, min(globalVars.uploadSize, (fileTotalCount - fileByteCount))))

       fileByteCount = fileByteCount + min(globalVars.uploadSize, (fileTotalCount - fileByteCount))

       consumer.start()
       producer.start()

       #Wait for upload to complete
       while producer.is_alive() or consumer.is_alive():
          producer.join(timeout=1.0)
          consumer.join(timeout=1.0)
