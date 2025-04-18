SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') CREATED_DATE
FROM USED_GOODS_BOARD B JOIN USED_GOODS_REPLY R
WHERE B.BOARD_ID = R.BOARD_ID
AND B.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY R.CREATED_DATE, B.TITLE