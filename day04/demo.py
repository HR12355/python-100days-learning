#じゃんけんゲーム
# 対戦形式
import random
rock = '''
　　　　　　　　　　　　　　　　.　-―- 　.
　　　　　　　　　　　　　　,. '´　　　　　　｀''ー-　 ､
　　　　　　　　　　 ,.-‐'´　　　　　　　　　　　　　　ヽ、
　　　　　　　　　,.:´　　　　　Y　　　　　　　　　　　　　ヽ、
　　 　 　 　 　 /　　 　 　 　 i　　　　　　　　　　　　　 　 ＼
.　　　　 　 　 .′　　　　　　 |　　 　 　 　 　 ∨　　　 　 　 .
　 　 　 　 ,.イ　　　　　 　 　 !　　　　 　 　　　'､　　　　　　　　ヽ
.　　　 　 .′　　　'.　　　　　 '.　　　　　　　　　 '. 　 /　 　 　 　 !
　　　　　i 　 　 　 ﾍ　　　　　ﾍ　　　　　　　　 　'.　ｆ　 　 　　　 }
　　　　　|　 　　　　ヽ　　　　　ヽ 　 　 　 　 　 　∨　 　 　 　 /｀
. 　 　　 .′　 　 　 　 ヽ　　　　　＼　　　　　 　　ｊ 　 　 　　. ′
　　　　 {　　 ＼　　　　　ヽ　　　　　＼　　　 　 ノ　　　　　/
.　　　　 '.　　　 ＼　　　　　 ヽ 　　　　｀ ー‐ｧ'´　　 　 　 /
　　　　　ヽ　　　　 ヽ 　　 　 　丶　　　 　／　　　　　 .:,.ｲ
　　　 　 　 ＼　　　　丶 　　　　　` ｰ‐ｧ'´　　　　 　 ／
　　　　　　 　 ＼　　　　 丶　　　　 ,.イ 　 　,..　-‐　´
　　　　　　 　 　 ` ‐- 　 .,＿,.＞‐''´　`ｰ一'
'''

scissors = '''
　　　　 　　　 　　 　, -､
　　　　　　　　　　　ｌ　　l
　　 ｒ　､　　 　　　　|　　|
　　 ｆ 　 ＼ 　　 　　|　　|
　 　 ＼　　＼　 　　|　　|
　　　　 ＼　　＼　　|　　|
　　　　 　 ＼　　＼.」　　|
　　 　 　 　 _入 　 　 　　ヽ
　 　　 　 r'　 ヽｊ　　‐--　　l
　　　　 ハ　 　 Y ｀ヽ＿ 　ハ
　　　　ヽ　＼　 ヽ、 　　 ￣｀ヽ
　　　　　 ＼_ ヽ _トﾆTヽ 　 　 |
　　　　　　　 }｀ ー' 〈　　　　　|
　　　　 　　　 ヾ _ 　 ヽ＿　　 |
　　　　　　　　 　 ＼ 　　　　　|
　　　　　　　　　　　|　　　　 　l
　　　　　　　　 　 　| 　 　 　　 l
　　　　　 　 　 　 　| 　 　 　 　 ｌ
　　　 　 　 　 　 　 | 　 　 　 　　ｌ
'''

paper = '''
.　 　 　 　ｒ 　､　　　 　ｆ ｀ｉ
　　　　　　＼　＼　 　 | 　!
　　　　ｒ　､ 　＼　＼ 　i 　ｉ　　　　　　　　　　 　 　 　 　 　 　 　 　⌒　､
　　　　 ＼ ＼ 　＼ 　､ｊ 　i　　　 　-､　　　　　　　　　　　　　／　　　 　 　､
　　　　　　＼ ＼__ﾉ 　 　 　、 ／　／　　　　　　　 　 　 　 　 　 　 　 　 　 ｉ
　　　 　 　 　 ヽ　 　 ,　´ ,　-'　　/　　　　　　　　　　　　　　　　 　 　 ｒ‐=≠=-　_　ｆ 7ヘ
　　 　ｒ‐―― ′　／ 　/　　 　ノ　　　　　　　　　　 　 　 　 　 　 ,ｨ':´}: : : : : : ヽ: : :`ｰ く
　 　 　` ｰ―　､　′　　　　 　/ }≧ ､　　　　　 　 　 　 　 　 　 /: : : ｊ: : ::Ｎｖ: : : ｖ:ﾍ : : ∧
　　　　　　　　 　､　 　 　 　 ノ}　ｉﾆﾆﾆヽ､　　　　　　　　　　 　/: : : :ハ: : { 　ヽ: : Ｖ∧: : :∧
　　　　　　　　　　ヽ _　　　´　ｊ　.}ﾆﾆﾆﾆﾆ`　､　　 　 　 　 　 /: : ::ｒﾆ ｉ.Ｖﾘ 伝ﾘ＼: }: : ｉ: : : ∧
　　　　　　　　　　　　　トｒ- ｙ'　/ﾆﾆﾆﾆﾆﾆﾆﾆヽ、　　　　 　〈: : : i{{　}}＿　ゝ.'　　}:i! : :! : : :}:∧
　　　　　　　　　　　　　{ {_　_／ﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆ≧ 、　　　　}: ::ｖ彡'　　　｀ヽ、 }:i: : :i: : : :}: : ｉ
　　　　　　　　　　　　　乂ﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆ＞ 、 　.}: :込　 　‐　　 　`ｊ/: : :i从ハ: : }
　　　　　　　　　　　　　　　`　＜ﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆ≧=‐‐‐≧ ､　　　_ イ: : :ﾊ}　　　∨
　　　　　　　　　　　　　　　　　　　　｀　　＜ﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆ≧＜￣｀ｉW
　　　　　　　　　　　　　　　　　　　　　　　　　`　＜ﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆ ｒ　´￣ `ｆｒ ⌒ヽ、
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　` ＜ﾆﾆﾆﾆﾆﾆﾆﾆ ﾑ　　　　}ヽ　　　＼
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 　｀ヽﾆﾆﾆﾆﾆﾆ ﾑ　　__ｊ 　ヽ　ｒ く
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　ヽﾆﾆﾆﾆﾆﾆﾆT　_ - ､i´＼ >
　　　　　　　　　　　　　　　　　　　　　　　　 　 　 　 　 　 　 　 　 ﾏﾆﾆﾆﾆﾆﾆ≦ﾆ とｒi}__/ﾆ.ﾑ
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 　 　 　 ﾏﾆﾆﾆﾆﾆﾆﾆﾆﾆ ＼/ﾆiﾆ.ﾑ
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 　 　 　 　 　 ﾏﾆﾆﾆﾆﾆﾆﾆﾆﾆOﾆﾆｉﾆﾆﾑ
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 　ﾏﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆ.iﾆﾆﾆﾑ
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　}ﾆﾆﾆﾆﾆﾆﾆﾆ Oﾆﾆﾏﾆﾆﾆﾑ
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 　ｊﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆｉﾏﾆﾆﾆ`､
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 　 　 　 　 　 /ﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆﾆ } ﾏﾆﾆﾆﾆヽ
'''

# print(paper)
choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

#CPUがランダムに値を出す。
# import random 一番上に書くのがマナー
print("CPU chose↓")
CPU = random.randint(0,2)
if CPU == 0:
    print(rock)
elif CPU == 1:
    print(paper)
elif CPU == 2:
    print(scissors)

# 勝ち負けの判定
# あいこ 引き分け
if choice == CPU:
    print("We draw!")
# 勝ち
if choice == 0 and CPU == 2:
    print("You win!")
if choice == 1 and CPU == 0:
    print("You win!")
if choice == 2 and CPU == 1:
    print("You win!")
# 負け
if choice == 0 and CPU == 1:
    print("You lose!")
if choice == 1 and CPU == 2:
    print("You lose!")
if choice == 2 and CPU == 0:
    print("You lose!")
