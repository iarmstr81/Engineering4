gpio -g mode 1 out
num=0 

while[ $num -le 19]
do
        /usr/bin/gpio -g toggle 1
        sleep .5
	let "num += 1"
	echo"$num"
done
gpio -g write 1 0 
