#/usr/bin/sh

for fn in `ls train/gt_img_*.txt`
do
    newname=`echo $fn | cut -d_ -f 2-3`
    #echo $fn '-->>'  'train/'$newname
    mv $fn 'train/'$newname
done