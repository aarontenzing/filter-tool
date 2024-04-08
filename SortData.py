import cv2
import os

class ImageClassifier:
    def __init__(self):
        self.directory = "data" # Directory containing images
        self.images = os.listdir(self.directory) # List of image file names (1_1.jpg, 1_2.jpg, ...)
        self.images.sort(key=self.images_sort)
        
        self.conditions = os.listdir("conditions") # List of condition file names (img1_1.jpg, img1_2.jpg, ...)
        self.conditions.sort(key=self.conditions_sort)
        
        self.total_images = len(self.images)
        self.current_index = 0
        self.window_name = 'Image Classifier'

    def conditions_sort(self, filename):
        parts = filename.split('_')
        return int(parts[0][3:]), int(parts[1].split('.')[0])
    
    def images_sort(self, filename):
        parts = filename.split('_')
        return int(parts[0]), int(parts[1].split('.')[0])

    def display_image(self):
        image_path = os.path.join(self.directory, self.images[self.current_index])
        self.image1 = cv2.imread(image_path)
        image_path = os.path.join("conditions\\", self.conditions[self.current_index])
        image2 = cv2.imread(image_path)        
        image = cv2.hconcat([self.image1, image2])
        cv2.imshow(self.window_name, image)
    
    def classify_image(self, status):
        # Save the image in the respective folder
        if status == 'good':
            print(f"Image {self.images[self.current_index]} classified as good")
            cv2.imwrite("dataset\\train\\good\\" + self.images[self.current_index], self.image1)
        elif status == 'bad':   
            print(f"Image {self.images[self.current_index]} classified as bad")
            cv2.imwrite("dataset\\train\\bad\\" + self.images[self.current_index], self.image1)    

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
    classifier = ImageClassifier()
    classifier.start_classification()
