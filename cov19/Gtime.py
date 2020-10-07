import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_conn():
    """
    连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="123456",
                           db="cov19",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    """
    封装通用查询

    返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_c1_data():
    """
     返回大屏div id=c1 的数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据,一下为改进代码
    sql = "select confirm,heal,dead from history order by ds desc limit 1"

    res = query(sql)
    return res[0]


def get_c2_data():
    """
   返回各省数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res


def get_l1_data():
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res


def get_l2_data():
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res


def get_r1_data():
    """
    返回非湖北地区城市确诊人数前10名
    """
    sql = 'SELECT city,confirm FROM ' \
          '(select city,confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆","香港","台湾","澳门") ' \
          'and city not in ("境外输入")'\
          'union all ' \
          'select province as city,sum(confirm) as confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆","香港","台湾","澳门") group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 10'
    res = query(sql)
    return res


def get_r2_data():
    """
   返回最近的热搜
    """
    sql = 'select content from hotsearch order by id desc limit 20'
    res = query(sql)
    return res
#('隔离期俄罗斯酒水销量激增217558',), ('美国全国均已宣布进入灾难状态218625',), ('意大利市长恳请复活节别外出226700',),

if __name__ == "__main__":
    print(get_r2_data())