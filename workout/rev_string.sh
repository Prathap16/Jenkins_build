read -p "enter string to reverse:" str
ength=${#str}
reverse=""
for((i = $length - 1; i >= 0; i--))
do
reverse=$reverse${str:i:1}
done
echo "$str reverse is $reverse"