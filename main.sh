INPUT_FOLDER="brains"
OUTPUT_FOLDER="skull_output"
BIAS_REDUCED_FOLDER="biasRed_output"

# Execute the hd-bet command
#hd-bet -i "$INPUT_FOLDER" -o "$OUTPUT_FOLDER" -device cpu -mode fast -tta 0

python3 bias_reduction.py "$OUTPUT_FOLDER" "$BIAS_REDUCED_FOLDER"
