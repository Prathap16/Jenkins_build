#Read the main string
echo "Enter the string:"
read mainstr

#Split the string based on the delimiter, ':'
readarray -d " " -t strarr <<< "$mainstr"
 echo "${strarr[*]}"
I=0
# Print each value of the array by using loop
for (( n=0; n < ${#strarr[*]}; n++))
do
  word=${strarr[n]}
  length=${#word}
  i=$(($length - 1))
  rev_word=""
  while [[ $i -ge 0 ]]
  do
  rev_word=$rev_word${word:i:1}
  let i--
  done
  #echo "$rev_word"
  final_arry+=("$rev_word")
  #echo "${final_arry[*]}"
  let I++
done
echo "${final_arry[*]}"
