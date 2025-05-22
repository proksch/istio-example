#!/bin/sh

V_OLD="$1"
V_NEW="$2"

# Check parameters are not empty
[ -z "$V_OLD" ] && { echo "Use: $0 <V_OLD> <V_NEW>"; exit 1; }
[ -z "$V_NEW" ] && { echo "Use: $0 <V_OLD> <V_NEW>"; exit 1; }
echo "Bumping from '$V_OLD' to '$V_NEW' ..."


replace_in_file() {
  FILE="$1"
  [ -f "$FILE" ] || { echo "Error: File $FILE not found"; return 1; }
  echo " - $FILE"

  sed "s/${V_OLD}/${V_NEW}/g" "$FILE" > "${FILE}.tmp"
  mv "${FILE}.tmp" "$FILE"
}

replace_in_file "README.md"
replace_in_file "app/app.py"
replace_in_file "lib/lib.py"
replace_in_file "operation/docker-compose.yml"
