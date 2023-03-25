from pathlib import Path

p1 = Path('files')
p2 = p1.glob("**/*")
for path in p2:
  if path.is_file():
    new_name = '-'.join(list(path.parts))
    new_path = path.with_name(new_name)
    path.rename(new_path)
    
    