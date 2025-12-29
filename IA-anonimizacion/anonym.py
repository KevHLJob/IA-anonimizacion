import cv2
from PIL import Image

# Path to the Haar Cascade XML file for face detection  source OPENCV
cls = 'haarcascade_frontalface_default.xml'

#function to anonymize faces in an image
def anonymize_image(outputfile, imagetoanonymise):
    # Read the image
    image = cv2.imread(imagetoanonymise)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Load the Haar Cascade for face detection
    facecascade = cv2.CascadeClassifier(cls)
    # Detect faces in the image
    faces = facecascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    # Anonymize each detected face
    for (a, b, c, d) in faces:
        face = image[b:b + d, a:a + c]
        blurredface= cv2.resize(cv2.resize(face, (c // 10, d // 10)), (c, d))
        image[b:b + d, a:a + c] = blurredface
    # Save the anonymized image
        cv2.imwrite(outputfile, image)
    # Return the anonymized image as a PIL Image object
        return Image.open(outputfile)


