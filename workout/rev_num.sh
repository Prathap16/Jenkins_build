read -p "enter number to reverse:" val
num=$val
#length=${#nmu}
echo "$length"
rem=0
rev=""
while [ $num -gt 0 ]
do
rem=$(( $num % 10 ))
num=$(( $num / 10 ))
#rev=$(( $rev * 10 + $rem ))
rev=$rev$rem
done
echo "$val reverse is $rev"