SELECT UGB.TITLE
      ,UGB.BOARD_ID
      ,UGR.REPLY_ID
      ,UGR.WRITER_ID
      ,UGR.CONTENTS
      ,DATE_FORMAT(UGR.CREATED_DATE, '%Y-%m-%d')
FROM USED_GOODS_BOARD UGB
JOIN USED_GOODS_REPLY UGR ON UGB.BOARD_ID = UGR.BOARD_ID 
WHERE UGB.CREATED_DATE LIKE '2022-10%'
ORDER BY UGR.CREATED_DATE, UGB.TITLE