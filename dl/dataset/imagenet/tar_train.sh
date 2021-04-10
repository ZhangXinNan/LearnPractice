# dir=/home/satisfie/imagenet/train #satisfie是我的用户名
mkdir ../train

for x in `ls *.tar`
do
	filename=`basename $x .tar` #注意空格
	mkdir ../train/$filename
	tar -xvf $x -C ../train/$filename
done

