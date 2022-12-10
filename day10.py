from functools import reduce

cycle_points = [20,60,100,140,180,220]
cycle_count = {
  "noop": 1,
  "addx": 2
}
signal_reports = []
crt_display = []

class CPU():
  cycles = 0
  scanline_position = 0
  registerX = 1
  current_display_line = []

  def check_cycle_count(self):
    """ if the cyclecount is one of the markers, note the signal"""
    if self.cycles in cycle_points:
      signal_reports.append(self.cycles * self.registerX)
  
  def draw_pixel(self) -> str:
    """ determine if the current pixel is lit or not """
    sprite = [self.registerX - 1, self.registerX, self.registerX + 1]
    if self.scanline_position-1 in sprite:
      return "#"
    return " "

  def execute_instruction(self, instruction: tuple):
    for i in range(0, cycle_count[instruction[0]]):
      self.cycles += 1
      self.scanline_position += 1
      self.check_cycle_count()
      self.current_display_line.append(self.draw_pixel())

      # see if the ray has reached the end of the display line
      if self.scanline_position == 40:
        crt_display.append(self.current_display_line)
        self.scanline_position = 0
        self.current_display_line = []

    if instruction[0] == "addx":
      self.registerX += int(instruction[1])

cpu = CPU()
with open("inputs/day10.txt") as f:
  data = [tuple(parts) for parts in [instr.rstrip().split(" ") for instr in f.readlines()]]

for instr in data:
  cpu.execute_instruction(instr)

print(signal_reports)
print("Day 10, part 1: {0}".format(reduce(lambda a, b: a + b, signal_reports)))
print("Day 10, part 2:")
for crt_line in crt_display:
  print("".join(crt_line))