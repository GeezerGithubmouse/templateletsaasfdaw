import urllib.request

# 优选 IP 来源列表
urls = [
    "https://bestcf.pages.dev/xinyitang3/ipv4.txt",
    "https://bestcf.pages.dev/tiancheng/all.txt",
    "https://bestcf.pages.dev/s5gy/mini.txt",
    "https://bestcf.pages.dev/cmliu/all.txt",
    "https://bestcf.pages.dev/uouin/all.txt",
    "https://bestcf.pages.dev/luoli/all.txt",
    "https://bestcf.pages.dev/lzj/all.txt",
    "https://raw.githubusercontent.com/ymyuuu/IPDB/refs/heads/main/BestCF/bestcfv4.txt",
    "https://bestcf.pages.dev/domain/qms/all.txt",
    "https://bestcf.pages.dev/ircf/ipv4.txt",
    "https://bestcf.pages.dev/domain/senflare/all.txt",
    "https://bestcf.pages.dev/nirevil/ipv4.txt",
    "https://bestcf.pages.dev/vvhan/ipv4.txt",
]

# 欧洲相关关键词列表（仅匹配带备注或明确标签的行）
EU_KEYWORDS = [
    "欧洲",
    "德国",
    "法国",
    "英国",
    "荷兰",
    "意大利",
    "西班牙",
    "瑞士",
    "瑞典",
    "波兰",
    "俄罗斯",
    "芬兰",
    "比利时",
    "奥地利",
    "GERMANY",
    "FRANCE",
    "UNITED KINGDOM",
    "NETHERLANDS",
    "EUROPE",
    "FRA",
    "MUC",
    "BER",
    "CDG",
    "LHR",
    "AMS",
]


def is_europe(line):
    """仅当存在备注且备注中明确包含欧洲相关地区词汇时，才判定为 True"""
    line_upper = line.upper()

    # 针对带有 # 备注的行进行精准提取与比对
    if "#" in line_upper:
        remark = line_upper.split("#", 1)[1]
        for kw in EU_KEYWORDS:
            if kw in remark:
                return True

    # 针对无 # 但用空格/连字符包含中文地名的行（如 "104.16.1.1 德国"）
    for cn_kw in [
        "欧洲",
        "德国",
        "法国",
        "英国",
        "荷兰",
        "意大利",
        "西班牙",
        "瑞士",
        "瑞典",
        "波兰",
        "俄罗斯",
    ]:
        if cn_kw in line_upper:
            return True

    return False


all_ips = set()
req_headers = {"User-Agent": "Mozilla/5.0"}

for url in urls:
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            lines = (
                response.read().decode("utf-8", errors="ignore").splitlines()
            )
            for line in lines:
                line = line.strip()
                # 剔除空白、整行注释行以及非 IP 协议行
                if (
                    line
                    and not line.startswith("#")
                    and not line.startswith("sub://")
                ):
                    # 仅在此处过滤掉带欧洲备注的节点
                    if not is_europe(line):
                        all_ips.add(line)
    except Exception:
        pass

# 排序并截取前 1000 个
sorted_ips = sorted(all_ips)[:1000]

with open("ip.txt", "w", encoding="utf-8") as f:
    for ip in sorted_ips:
        f.write(ip + "\n")
