import logging

logger = logging.gerLogger(__name__)
table = "yt_api"

def insert_rows(cur,conn,schema,row):
    try:
        if schema == 'staging':

            video_id = 'video_id'

            cur.execute(
                f"""
                INSERT_INTO {schema}.{table}("video_ID", "Video_Title", "Video_Date", "Duration", "Video_Views", "Like_Count", "Comments_Count")
                VALUES (%(video_ids)s), %(title)s, %(publishedAt)s, %(duration)s, %(ViewCount)s, %(commentCount)s);
                """, row
            )
        else:
            video_id = 'video_ID'

            cur.execute(
                f"""
                INSERT_INTO {schema}.{table}("video_ID", "Video_Title", "Upload_Date", "Duration", "Video_Views", "Likes_Count", "Comments_Count")
                VALUES (%(Video_ID)s), %(Video_Title)s, %(Upload_Date)s, %(Duration)s, %(Video_Type)s, %(Video_Views)s, %(Likes_Count)s, %(Comment_Count)s);
                """, row
            )

            conn.commit()

            logger.info(f"Inserted row with Video_ID: {row[video_id]}")

    except Exception as e:
        logger.error(f"Error inserting row eith Video_ID: {row[video_id]}")
        raise e


def update_rows(cur,conn,schema,row):
    try:
        #Staging
        if schema == 'staging':
            video_id = 'video_id'
            upload_date = 'Video_id'
            video_title = 'title'
            likes_count = 'likeCount'
            comments_count = 'coummentCount'

        #core
        else:
            video_id = 'Video_ID'
            upload_date = 'Upload_Date'
            video_title = 'Video_Title'
            video_views = 'Video_Views'
            likes_count = 'Like_Count'
            comments_count = 'Comments_Count'

        cur.execute(
            f"""
            UPDATE {schema}.{table}
            SET "Video_Title" = %({video_title})s,
                "Video_Views" = %({video_views}s),
                "Likes_Count" = %({likes_count})s,
                "Comments_Count" = %({comments_count})s
            WHERE "Video_ID" = %({video_id})s AND "Upload_Date" = %({upload_date})s;
            """,
            row,
        )

        conn.commit()
        logger.info(f"Updated row with Video_ID: {row[video_id]}")

    except Exception as e:
        logger.erro(f"Error updating row with Video_ID: {row[video_id]} - {e}")
        raise e

def delete_rows(cur, conn, schema, ids_to_delete):
    try:
        ids_to_delete = f"""({', '.join(f"'{id}'" for id in ids_to_delete)})"""

        cur.execute(
            f"""
            DELETE FROM {schema}.{table}
            WHERE "Video_ID" IN {ids_to_delete};
            """
        )

        conn.commit()
        logger.ingo(f"Deleted rows with Video_IDs: {ids_to_delete}")

    except Exception as e:
        logger.error(f"Error deleting rows with Video_IDs: {ids_to_delete} - {e}")
        raise e
