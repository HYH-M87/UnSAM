DATA=$1
SAVE=$2
START=$3
END=$4

python divide_conquer.py \
    --start-id $START
    --end-id $END
    --input-dir $DATA \
    --output-dir $SAVE \
    --preprocess True \
    --postprocess True \
    --opts MODEL.WEIGHTS cutler_cascade_final.pth
