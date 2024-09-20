import pyautogui
import time
import requests
import json

print(pyautogui.position())
print(pyautogui.size())
# for _ in range(10):
#     pyautogui.moveTo(x=1401, y=374)
#     pyautogui.click()
#     time.sleep(3)
#     pyautogui.moveTo(x=1319, y=402)
#     pyautogui.click()
#     time.sleep(15)
#     pyautogui.moveTo(x=1325, y=520)
#     print("広告１開始")
#     time.sleep(80)
#     print("広告１終了")
#     pyautogui.moveTo(x=1446, y=134)
#     pyautogui.click()
#     pyautogui.click()
#     pyautogui.moveTo(x=1206, y=143)
#     pyautogui.click()
#     time.sleep(10)
#     pyautogui.moveTo(x=1446, y=134)
#     pyautogui.click()
#     print("広告２開始")
#     time.sleep(10)
#     print("広告２終了")
#     pyautogui.moveTo(x=1446, y=134)
#     pyautogui.click()
#     pyautogui.click()
#     time.sleep(5)
#     pyautogui.moveTo(x=1324, y=463)
#     pyautogui.click()
#     pyautogui.click()
#     print("報酬ゲット")
#     time.sleep(15)

#WEB_HOOK_URLに、さっき発行したURLを設定
WEB_HOOK_URL = "https://hooks.slack.com/services/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"

requests.post(WEB_HOOK_URL, data=json.dumps({
    #メッセージ
    "text" : "ANA Pocket のチャレンジ広告視聴が終了したよ",
}))