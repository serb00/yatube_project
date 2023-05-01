SELECT
    "posts_post"."id",
    "posts_post"."text",
    "posts_post"."pub_date",
    "posts_post"."author_id",
    "posts_post"."group_id"
FROM
    "posts_post"
WHERE
    "posts_post"."author_id" = 3