def to_num(card):
  """num"""
  if card[0].isdigit():
    return int(card[0])
  else:
    nums = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14}
    if card[0] in nums:
      return nums[card[0]]

a=input().replace(',', '').replace("'", '')[1:-1].split(' ')
b=input().replace(',', '').replace("'", '')[1:-1].split(' ')
aa=list(map(to_num, a))
bb=list(map(to_num, b))
if sum(aa)>sum(bb):
  print("Player 1")
else:print("Player 2")