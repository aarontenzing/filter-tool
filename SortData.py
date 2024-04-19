import cv2
import os
import uuid

class ImageClassifier:
    def __init__(self, type="train"):
        self.directory = "data" # Directory containing images
        
        self.images = os.listdir(self.directory) # List of image file names (1_1.jpg, 1_2.jpg, ...)
        self.images = sorted(self.images, key=lambda x: (int(x.split('_')[0]), int(x.split('_')[1].split('.')[0])))
        
        self.conditions = os.listdir("wireframes") 
        self.conditions = sorted(self.conditions, key=lambda x: (int(x.split('_')[0]), int(x.split('_')[1].split('.')[0])))
        
        self.total_images = len(self.images)
        self.current_index = 0
        self.window_name = 'Image Classifier'
                        
        self.type = type

    def display_image(self):
        print(self.images[self.current_index], self.conditions[self.current_index])
        image_path = os.path.join(self.directory, self.images[self.current_index])
        self.image1 = cv2.imread(image_path)
        image_path = os.path.join("wireframes\\", self.conditions[self.current_index])
        image2 = cv2.imread(image_path)        
        image = cv2.hconcat([self.image1, image2])
        cv2.imshow(self.window_name, image)
    
    def classify_image(self, status):
        # Save the image in the respective folder
        unique_id = str(uuid.uuid4())
        print(unique_id)
        if status == 'good':
            print(f"Image {self.images[self.current_index]} classified as good")
            cv2.imwrite("dataset\\"+self.type+"\\good\\"+unique_id+".jpg", self.image1)
        elif status == 'bad':   
            print(f"Image {self.images[self.current_index]} classified as bad")
            cv2.imwrite("dataset\\"+self.type+"\\bad\\"+ unique_id+".jpg", self.image1)    

        print("classified images: ", self.current_index + 1, "out of", self.total_images)

    def start_classification(self):
        cv2.namedWindow(self.window_name)
        self.display_image()

        while True:    
            key = cv2.waitKey(0)
            if key == ord('q'):  # ESC key to exit
                break   
            elif key == ord('g'):  # 'a' key for bad classification
                self.classify_image('good')
                self.current_index += 1
                if self.current_index < self.total_images:
                    self.display_image()
                else:
                    print("All images classified")
                    break
            elif key == ord('b'):  # 'd' key for good classification
                self.classify_image('bad')
                self.current_index += 1
                if self.current_index < self.total_images:
                    self.display_image()
                else:
                    print("All images classified")
                    break
                
        cv2.destroyAllWindows()

if __name__ == "__main__":
    classifier = ImageClassifier(type="train")
    classifier.start_classification()
