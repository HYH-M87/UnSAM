DATA=$1
SAVE=$2
python divide_conquer.py \
    --input-dir $DATA \
    --output-dir $SAVE \
    --preprocess True \
    --postprocess True \
    --opts MODEL.WEIGHTS cutler_cascade_final.pth
