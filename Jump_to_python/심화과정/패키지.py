# Pakage
"""
game
   - __init__.py
   - sound
      - __init__.py
      _ echo.py
   - graphic
      - __init__.py
      - render.py
"""
# echo.py
"""
def echo_test():
    print("echo")
"""

# render.py
"""
def render_test():
    print("render")
"""

# 가상의 game 패키지

#1
import game.sound.echo
game.sound.echo.echo_test()         #echo

#2
from game.sound import echo
echo.echo_test()                    #echo

#3
from game.sound.echo import echo_test
echo_test()                         #echo

# __init__.py의 용도
# 해당 디렉터리가 패키지의 일부임을 알려주는 역할

# relative 패키지
# render.py
"""
from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()
"""

from game.graphic.render import render_test
render_test()
# render
# echo

