from settings import Settings
import cv2



class Display:
    """A class to store the different display screens"""

    def __init__(self):
        self.settings = Settings()

    #Static Screens
    def start_screen(self, frame):
        """Start Screen for Sketch It"""
        cv2.putText(frame, "Welcome to 'Can you draw?''",(10, self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, self.settings.font_size, self.settings.font_color, 2)

        cv2.putText(frame, "Press (s) to start",(10,frame.shape[0]-2*self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, self.settings.font_size, self.settings.font_color, 2)

        cv2.putText(frame, "Press (c) to calibrate background",(10,frame.shape[0]-self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, self.settings.font_size, self.settings.font_color, 2)

        cv2.imshow("CAN YOU DRAW",frame)

    def calibration_screen(self, frame):
        """Calibration Screen for Sketch It"""
        cv2.putText(frame, 'Calibrating Background',(10,self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, self.settings.font_size, (0, 0, 0), 2)

        cv2.putText(frame, 'Press (y) to Continue',(10,frame.shape[0]-self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, self.settings.font_size, (0, 0, 0), 2)

        cv2.imshow("CAN YOU DRAW",frame)


    #Dynamic Screens
    def level_screen(self, frame, object_str, object_detection, answer, contour_dimensions = None):
        """Display screen of current level"""

        cv2.putText(frame, 'Lets see you draw a {}'.format(object_str),(10,self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, int(self.settings.font_size*1.5), self.settings.font_color, 2)

        cv2.putText(frame, 'Sketch: {}'.format(object_detection),(10,2*self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, self.settings.font_size, self.settings.font_color, 2)


        cv2.putText(frame, "{}".format(answer), (10, frame.shape[0]-self.settings.font_y_pad),
            cv2.FONT_HERSHEY_SIMPLEX, self.settings.font_size, self.settings.font_color, 2)

        #if contour_dimensions are given, draw bounding box
        if contour_dimensions:
            x, y, w, h = contour_dimensions[0], contour_dimensions[1], contour_dimensions[2], contour_dimensions[3]

            #draws a bounding box around the detected object
            cv2.rectangle(frame, (x-20,y-20),(x+w+20, y+h+20),
                (0,255,0),2)

        cv2.imshow("CAN YOU DRAW",frame)
