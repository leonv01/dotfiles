import os
import json
import shutil

mounts = ["/", "/mnt/disk1", "/mnt/disk2"]

index_file = "/tmp/waybar_disk_index"

index = 0

if not os.path.exists(index_file):
    index = 0
else:
    with open(index_file, "r") as f:
        try:
            index = int(f.read().strip())
        except ValueError:
            index = 0

index = (index + 1) % len(mounts)
with open(index_file, "w") as f:
    f.write(str(index))

mount = mounts[index]

try:
    total, used, free = shutil.disk_usage(mount)
    if free > 1024**3:
        avail_str = f"{free // (1024**3)} GiB"
    elif free > 1024**2:
        avail_str = f"{free // (1024**2)} MiB"
    else:
        avail_str= f"{free // 1024} KiB"
    text = f" {avail_str}"
    tooltip = f"{mount} has {avail_str} free"
except:
    text = "N/A"
    tooltip = f"Mount point not found: {mount}"

print(json.dumps({
    "text": text,
    "tooltip": tooltip
}))
