
import os
import sys

paddle_ocr_dir = os.path.join(os.getenv('HOME'), 'github/PaddleOCR')
sys.path.append(paddle_ocr_dir)
print(paddle_ocr_dir)

import cv2
import copy
import logging
import numpy as np
import time
import tools.infer.predict_rec as predict_rec
import tools.infer.predict_det as predict_det
import tools.infer.utility as utility
from tools.infer.predict_system import sorted_boxes
from ppocr.utils.utility import get_image_file_list, check_and_read
from ppocr.utils.logging import get_logger
from ppstructure.table.matcher import TableMatch
from ppstructure.table.table_master_match import TableMasterMatcher
from ppstructure.utility import parse_args
import ppstructure.table.predict_structure as predict_strture
from ppstructure.table.predict_table import TableSystem


logger = get_logger()


def main(args):
    image_file_list = get_image_file_list(args.image_dir)
    image_file_list = image_file_list[args.process_id::args.total_process_num]
    os.makedirs(args.output, exist_ok=True)

    table_sys = TableSystem(args)
    img_num = len(image_file_list)

    f_html = open(
        os.path.join(args.output, 'show.html'), mode='w', encoding='utf-8')
    f_html.write('<html>\n<body>\n')
    f_html.write('<table border="1">\n')
    f_html.write(
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />"
    )
    f_html.write("<tr>\n")
    f_html.write('<td>img name\n')
    f_html.write('<td>ori image</td>')
    f_html.write('<td>table html</td>')
    f_html.write('<td>cell box</td>')
    f_html.write("</tr>\n")

    for i, image_file in enumerate(image_file_list):
        logger.info("[{}/{}] {}".format(i, img_num, image_file))
        img, flag, _ = check_and_read(image_file)
        excel_path = os.path.join(
            args.output, os.path.basename(image_file).split('.')[0] + '.xlsx')
        if not flag:
            img = cv2.imread(image_file)
        if img is None:
            logger.error("error in loading image:{}".format(image_file))
            continue
        starttime = time.time()
        pred_res, _ = table_sys(img)
        pred_html = pred_res['html']
        logger.info(pred_html)
        to_excel(pred_html, excel_path)
        logger.info('excel saved to {}'.format(excel_path))
        elapse = time.time() - starttime
        logger.info("Predict time : {:.3f}s".format(elapse))

        if len(pred_res['cell_bbox']) > 0 and len(pred_res['cell_bbox'][
                0]) == 4:
            img = predict_strture.draw_rectangle(image_file,
                                                 pred_res['cell_bbox'])
        else:
            img = utility.draw_boxes(img, pred_res['cell_bbox'])
        img_save_path = os.path.join(args.output, os.path.basename(image_file))
        cv2.imwrite(img_save_path, img)

        f_html.write("<tr>\n")
        f_html.write(f'<td> {os.path.basename(image_file)} <br/>\n')
        f_html.write(f'<td><img src="{image_file}" width=640></td>\n')
        f_html.write('<td><table  border="1">' + pred_html.replace(
            '<html><body><table>', '').replace('</table></body></html>', '') +
                     '</table></td>\n')
        f_html.write(
            f'<td><img src="{os.path.basename(image_file)}" width=640></td>\n')
        f_html.write("</tr>\n")
    f_html.write("</table>\n")
    f_html.close()

    if args.benchmark:
        text_sys.autolog.report()


if __name__ == "__main__":
    args = parse_args()
    main(args)