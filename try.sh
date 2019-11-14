

while IFS= read -r line
do
echo "$line"
echo "\"$line\""": 1," >>words.json

done <"words.txt"