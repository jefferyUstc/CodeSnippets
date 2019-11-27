indir=$1
outdir=$2
rate=$3

mkdir -p "$outdir"

for file in "$indir"/*.bed
do
  echo "$file"
  count=$(wc -l "$file" | awk '{print $1}')
  count=$(echo "$count"*"$rate" | bc)
  count=${count%.*}
  basename=${file##*/}

  for i in $(seq 1 5)
  do
    seq_num=$(echo "$i")
    shuf -n "$count" "$file" -o "$outdir"/"${basename%%.*}"."$seq_num".bed;
  done
done