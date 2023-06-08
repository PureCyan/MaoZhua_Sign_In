import argparse
from login import login
from click_sign import sign
from comment import get_links, random_links, comment

parser = argparse.ArgumentParser()
parser.add_argument("--pd", help="password of MaoZhua", required=True)
parser.add_argument("--acc", help="account of MaoZhua", required=True)
args = parser.parse_args()

# 登录
browser = login("https://maozhua.org/", args.pd, args.acc)

# 签到
#sign(browser, "https://maozhua.org/mission/today")

# 评论
links = get_links("https://maozhua.org/tags")
random_link = random_links(links)
for element in random_link:
  comment(browser, element)
