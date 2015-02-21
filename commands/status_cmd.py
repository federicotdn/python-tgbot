import subprocess
from bot import command, msg

class StatusCmd(command.BotCommand):
    def run(self, dest, contents):
      commit = 'commit hash: ' + self.process_output('git rev-parse --short HEAD') + '...'
      uptime = self.process_output('uptime -p')
      free = self.process_output('free -m').split('\n')[1].split()
      total = int(free[1])
      used = int(free[2])
      used_percentage = int(used / total * 100)

      resp = msg.BotMsg(commit)
      resp.add_line('uptime: ' + uptime)
      resp.add_line('Memory used: ' + str(used_percentage) + '%')
      return resp

    def process_output(self, command):
      return subprocess.check_output(command.split()).decode().strip()

command_instance = StatusCmd(commands = ['status'], name = 'status')