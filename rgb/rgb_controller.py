
# Capture RGB Image or at least fake it
# xpospi27
from datetime import datetime
import random
# from pypylon import pylon
import platform
import shutil

cam = None

class RGB:

    # def isCameraAvailable():
    #     try:
    #         pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    #         return True
    #     except:
    #         return False

    def returnFakeImage(folder, filename):
        src="rgb/examples/%d.png" % random.randint(1,3)
        dst=f"{folder}/{filename}_%d.png" % 1
        shutil.copy(src,dst)

    # def captureImage(folder="rgb/output", number=1):
    #     timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    #     if(RGB.isCameraAvailable()):
    #         img = pylon.PylonImage()
    #         tlf = pylon.TlFactory.GetInstance()
    #
    #         cam = pylon.InstantCamera(tlf.CreateFirstDevice())
    #         cam.Open()
    #         cam.StartGrabbing()
    #
    #         for i in range(number):
    #             with cam.RetrieveResult(2000) as result:
    #                 img.AttachGrabResultBuffer(result)
    #
    #                 if platform.system() == 'Windows':
    #                     ipo = pylon.ImagePersistenceOptions()
    #                     quality = 90 - i * 10
    #                     ipo.SetQuality(quality)
    #                     filename = "{folder}/{filename}_%d.jpeg" % quality
    #                     img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
    #                 else:
    #                     filename = "{folder}/{filename}_%d.png" % i
    #                     img.Save(pylon.ImageFileFormat_Png, filename)
    #                 img.Release()
    #         cam.StopGrabbing()
    #         cam.Close()
    #
    #     else:
    #         print("Error - camera not found")

    def captureFakeImage(folder="rgb/output", number=1):
        timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        RGB.returnFakeImage(folder, timestamp)

