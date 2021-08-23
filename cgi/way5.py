#!/usr/bin/python3
import cgi
import subprocess
import boto3
import os
print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()
form = cgi.FieldStorage()
fileitem = form['filename']
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'
print("\n")
print(message)
#print(\n)
#print(filename)
#print('/tmp/' + fn)
#print(/tmp/ + fn)
"""import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'

print """\
#Content-Type: text/html\n
#<html>
#<body>
 #  <p>%s</p>
#</body>
#</html>
""" % (message,)

print "hello"
print "%s" % (fileitem.filename)
print "%s" % (fn)
"""



#import boto3


region= "us-west-1"
bucket = "team12345"
upimage = "file2.jpg"
myphoto = '/tmp/' + fn
print("\n")
#print(region)
#print(myphoto)

def face_reader():
    try:
        s3 = boto3.resource('s3')
        s3.Bucket(bucket).upload_file(myphoto , upimage)
        #print(myphoto)
        rek = boto3.client('rekognition' , region )
        response = rek.detect_labels(
        Image={

                'S3Object': {
                    'Bucket': bucket,
                    'Name': upimage,
                }
            },
            MaxLabels=10,
            MinConfidence=50
        )

       # print("hello")
        print("\n")
        print("DETECTED OBJECTS GIVEN BELOW:-")
        for i in range(10):
            print("\n")
            print(response['Labels'][i]['Name'])
            if response['Labels'][i]['Name'] == "Man":
                smile = "Your Gender is Male"
                # output = subprocess.getoutput("Your Gender is Male")
                #  print(output)
                print("\n")
                print(smile)
                    #voice(man)
            if response['Labels'][i]['Name'] == "Woman":
                smile = "Your Gender is FeMale"
                   # print(\n)
                print("\n")
                print(smile)
                        #voice(man)
                    #if response['Labels'][i]['Name'] != "Chair":
                      #  break
            if response['Labels'][i]['Name'] == None:
                smile = "Objects Not Available"
                print("\n")
                print(smile)

        print("\n")
        print("DETECTED FACE GESTURES GIVEN BELOW:-")
        resfaces = rek.detect_faces(
            Image={

                'S3Object': {
                    'Bucket': bucket,
                    'Name': upimage,

                }
            },
            Attributes=['ALL'])


        if  resfaces['FaceDetails'][0]['Smile']['Value'] == False:
            smile = "PLease Smile You Look Like Sad"
            #voice(smile)
           # print(\n)
            print("\n")
            print(smile)
        if  resfaces['FaceDetails'][0]['Eyeglasses']['Value'] == True:
            smile = "Ohh I Think You Wear A Eyeglasses"
            #voice(smile)
            print("\n")
            print(smile)
        if  resfaces['FaceDetails'][0]['Sunglasses']['Value'] == True:
            smile = "Ohh I Think You Wear A Sunglasses"
        # voice(smile)
            print("\n")
            print(smile)
        if  resfaces['FaceDetails'][0]['Beard']['Value'] == True:
            smile = "You Have A Beard Please Shave Your Beard"
            #voice(smile)
            print("\n")
            print(smile)
        if  resfaces['FaceDetails'][0]['Mustache']['Value'] == True:
            smile = "You Have also mustache"
        # voice(smile)
            print("\n")
            print(smile)

        # voice(smile)
        if resfaces['FaceDetails'][0]['AgeRange']['Low'] > 0 :
            min_age=(resfaces['FaceDetails'][0]['AgeRange']['Low'])
            max_age=(resfaces['FaceDetails'][0]['AgeRange']['High'])
            smile = "Your Age Is Between" + str(min_age) + "year to" + str(max_age) + "year"
        # voice(age)
            print("\n")
            print(smile)
        if resfaces['FaceDetails'][0]['EyesOpen']['Value'] == True:
            smile = "Your Eyes is Open"
            print("\n")
            print(smile)
        # voice(smile)
        if resfaces['FaceDetails'][0]['MouthOpen']['Value'] == True:
            smile = "Your Mouth is Open"
            #voice(smile)
            print("\n")
            print(smile)
        for i in range(7):
        # print(resfaces['FaceDetails'][0]['Emotions'][i]['Confidence'])
            if (resfaces['FaceDetails'][0]['Emotions'][i]['Confidence']) > 50.0000 :
                emotion=(resfaces['FaceDetails'][0]['Emotions'][i]['Type'])
                smile = "Your Face Emotion is" + emotion
                #voice(emo)
                print("\n")
                print(smile)

    except Exception as error_msg:
        print(error_msg)

face_reader()
