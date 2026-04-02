{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "842d64ad-1cf0-4563-8c68-4100e3666bf2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Get ready! Recording 'Good' in 3 seconds...\n",
      "Recording 1/20: Good_1.mp4\n",
      "Recording 2/20: Good_2.mp4\n",
      "Recording 3/20: Good_3.mp4\n",
      "Recording 4/20: Good_4.mp4\n",
      "Recording 5/20: Good_5.mp4\n",
      "Recording 6/20: Good_6.mp4\n",
      "Recording 7/20: Good_7.mp4\n",
      "Recording 8/20: Good_8.mp4\n",
      "Recording 9/20: Good_9.mp4\n",
      "Recording 10/20: Good_10.mp4\n",
      "Recording 11/20: Good_11.mp4\n",
      "Recording 12/20: Good_12.mp4\n",
      "Recording 13/20: Good_13.mp4\n",
      "Recording 14/20: Good_14.mp4\n",
      "Recording 15/20: Good_15.mp4\n",
      "Recording 16/20: Good_16.mp4\n",
      "Recording 17/20: Good_17.mp4\n",
      "Recording 18/20: Good_18.mp4\n",
      "Recording 19/20: Good_19.mp4\n",
      "Recording 20/20: Good_20.mp4\n",
      "✅ Recording completed\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import os\n",
    "import time\n",
    "\n",
    "SIGN_NAME = \"Good\"\n",
    "NUM_VIDEOS = 20\n",
    "DURATION = 2               # seconds\n",
    "FPS = 30\n",
    "PREP_TIME = 3              # get ready time\n",
    "BREAK_TIME = 1             # break between recordings\n",
    "\n",
    "BASE_DIR = os.getcwd()\n",
    "SAVE_DIR = os.path.join(BASE_DIR, \"MP_Data\", SIGN_NAME)\n",
    "os.makedirs(SAVE_DIR, exist_ok=True)\n",
    "\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))\n",
    "height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))\n",
    "\n",
    "print(f\"Get ready! Recording '{SIGN_NAME}' in {PREP_TIME} seconds...\")\n",
    "time.sleep(PREP_TIME)\n",
    "\n",
    "for i in range(1, NUM_VIDEOS + 1):\n",
    "    filename = f\"{SIGN_NAME}_{i}.mp4\"\n",
    "    filepath = os.path.join(SAVE_DIR, filename)\n",
    "\n",
    "    fourcc = cv2.VideoWriter_fourcc(*'mp4v')\n",
    "    out = cv2.VideoWriter(filepath, fourcc, FPS, (width, height))\n",
    "\n",
    "    print(f\"Recording {i}/{NUM_VIDEOS}: {filename}\")\n",
    "\n",
    "    start_time = time.time()\n",
    "    while time.time() - start_time < DURATION:\n",
    "        ret, frame = cap.read()\n",
    "        if not ret:\n",
    "            break\n",
    "\n",
    "        cv2.putText(frame, f\"{SIGN_NAME} ({i}/{NUM_VIDEOS})\",\n",
    "                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,\n",
    "                    1, (0, 255, 0), 2)\n",
    "\n",
    "        out.write(frame)\n",
    "        cv2.imshow(\"Hand2Voice Recorder\", frame)\n",
    "        cv2.waitKey(1)\n",
    "\n",
    "    out.release()\n",
    "    time.sleep(BREAK_TIME)\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n",
    "print(\"✅ Recording completed\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9b35882f-23a3-405e-b2a1-272a8a683d08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Files in Hello folder:\n",
      "['Good_1.mp4', 'Good_10.mp4', 'Good_11.mp4', 'Good_12.mp4', 'Good_13.mp4', 'Good_14.mp4', 'Good_15.mp4', 'Good_16.mp4', 'Good_17.mp4', 'Good_18.mp4', 'Good_19.mp4', 'Good_2.mp4', 'Good_20.mp4', 'Good_3.mp4', 'Good_4.mp4', 'Good_5.mp4', 'Good_6.mp4', 'Good_7.mp4', 'Good_8.mp4', 'Good_9.mp4']\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "path = \"MP_Data/Good\"\n",
    "print(\"Files in Hello folder:\")\n",
    "print(os.listdir(path))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f79d7fb4-253a-447a-8e77-643c2805e273",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:hand2voice]",
   "language": "python",
   "name": "conda-env-hand2voice-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
