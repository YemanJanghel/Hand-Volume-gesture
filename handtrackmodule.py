import cv2
import mediapipe as mp
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, image, draw=True):
            imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.results = self.hands.process(imageRGB)

            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
            return image

    def findPosition(self, image, handNo=0, draw=True):
            lmlist = []
            if self.results.multi_hand_landmarks:
                Hand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(Hand.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmlist.append([id, cx, cy])
                    if draw:
                        cv2.circle(image, (cx, cy), 10, (255, 255, 0), cv2.FILLED)

            return lmlist

def main():
        cap = cv2.VideoCapture(0)
        tracker = handDetector()

        while True:
                success, image = cap.read()
                image = tracker.findHands(image)
                lmList = tracker.findPosition(image)
                if len(lmList) != 0:
                    print(lmList[4])

                cv2.imshow("Video", image)
                cv2.waitKey(1)
if __name__ == "__main__":
 main()