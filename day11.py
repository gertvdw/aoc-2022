from math import floor
from functools import reduce
import re

class Monkey:
  def __init__(self):
    self.id = 0
    self.items = []
    self.operation = lambda x: x
    self.test_divisor = 1
    self.target_monkeys = [0, 0]
    self.inspect_count = 0

  def receive_thrown_item(self, item):
    self.items.push(item)

  def inspect(self, very_worried=False):
    for item in self.items:
      self.inspect_count += 1
      # print("Inspecting {}".format(item))
      # after inspection, worry level increases with operation
      worry_level = eval(self.operation)
      # print("worry level: {}".format(worry_level))

      # monkey gets bored. divide by 3, round to nearest int.
      if not very_worried:
        worry_level = floor(worry_level / 3)
        # print("after bored: {}".format(worry_level))
      
      # this was actually for part 2, but applies to part 1 as well.
      divisors = reduce(lambda acc,b: acc * b, [m.test_divisor for m in monkeys])
      worry_level = worry_level % divisors
      # if dividing by test_divisor is a whole number, throw
      # to target_monkey 0
      # else target_monkey 1
      yield worry_level, self.target_monkeys[0] if worry_level % self.test_divisor == 0 else self.target_monkeys[1]
    self.items.clear()


def init_monkeys():
  monkeys = []
  with open("inputs/day11.txt") as f:
    current_monkey = Monkey()
    for line in [line.rstrip() for line in f.readlines()] + ['']:
      id = re.match(r'Monkey (\d):', line)
      if id:
        current_monkey.id = int(id.group(1))
        continue
      starting_items = re.match(r'.*?Starting items: (.*)', line)
      if starting_items:
        current_monkey.items = [int(item) for item in starting_items.group(1).replace(" ", "").split(",")]
        continue
      operation = re.match(r'.*?Operation: new = (.*)', line)
      if operation:
        op = operation.group(1).replace("old", "item")
        current_monkey.operation = "{}".format(op)
        continue
      test = re.match(r'.*?Test: divisible by (\d+)', line)
      target_if_true = re.match(r'.*?If true: throw to monkey (\d+)', line)
      target_if_false = re.match(r'.*?If false: throw to monkey (\d+)', line)
      if test:
        current_monkey.test_divisor = int(test.group(1))
        continue
      if target_if_true:
        current_monkey.target_monkeys[0] = int(target_if_true.group(1))
        continue
      if target_if_false:
        current_monkey.target_monkeys[1] = int(target_if_false.group(1))
        continue
      if line == "":
        monkeys.append(current_monkey)
        current_monkey = Monkey()
  return monkeys

monkeys = init_monkeys()
# for m in monkeys:
#   print("monkey: {0}".format(m.id))
#   print(" starting items: {0}".format(m.items))
#   print(" operation: {0}".format(m.operation))
#   print(" test_divisor: {0}".format(m.test_divisor))
#   print(" target_monkeys: {0}".format(m.target_monkeys))

for i in range(0, 20):
  for m in monkeys:
    thrown_items = [inspection_result for inspection_result in m.inspect()]
    for t in thrown_items:
      monkeys[t[1]].items.append(t[0])
      

top_two_simians = sorted(monkeys, key=lambda a: a.inspect_count, reverse=True)[0:2]
print("Day 11, part 1: monkeybusiness = {}".format(top_two_simians[0].inspect_count * top_two_simians[1].inspect_count))

monkeys = init_monkeys()
for i in range(0, 10000):
  for m in monkeys:
    thrown_items = [inspection_result for inspection_result in m.inspect(very_worried=True)]
    for t in thrown_items:
      monkeys[t[1]].items.append(t[0])

top_two_simians = sorted(monkeys, key=lambda a: a.inspect_count, reverse=True)[0:2]
print("Day 11, part 1: monkeybusiness = {}".format(top_two_simians[0].inspect_count * top_two_simians[1].inspect_count))