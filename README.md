# 模型 × 思考强度对照实验

2026-11-03 完成的三轮实验，覆盖 6 个请求模型名称、35 个可执行模型与思考强度组合。

## 下载完整资料

**[下载三轮完整 ZIP（14.5 MB）](https://github.com/yfkoria/competition/raw/refs/heads/main/model_comparison_v3_complete.zip)**

完整包包含三轮原始答卷与源码、语言风格盲评、固定题包和输入、程序输出、编译与判题日志、异常诊断、分析报告、评分 CSV、冻结规则、哈希与复算脚本。原始 ZIP 未重新打包。

- [第一轮：能力与语言风格报告](reports/round-1.txt) · [结果 CSV](results/round-1.csv)
- [第二轮：压力测试与异常分析](reports/round-2.txt) · [结果 CSV](results/round-2.csv)
- [第三轮：连续优化任务报告](reports/round-3.txt) · [全部 35 配置 CSV](results/round-3.csv)
- [第三轮完整矩阵图](figures/round-3.svg)
- [ZIP 的 SHA-256](archive.sha256)

## 主要结果

第三轮固定三个 Frontier-CS 公开任务，每个配置每题生成一次程序，共105份程序。统一题包、8个固定输入、GNU C++17/-O2、单核、每输入2秒CPU/5秒墙钟/512MiB。

上一轮共同满分的 Astra、6.1 Sol、6 Sol 的 xhigh/max/ultra 九格，本轮装箱质量为86.46—96.81，相差10.36分，且全部输出合法。调度与最大割仍只有1.81和0.51分差，Astra与6.1 Sol仍接近。

| 请求模型 | max 装箱 | max 调度 | max 最大割 |
|---|---:|---:|---:|
| 6 Astra | 96.81 | 89.68 | 87.57 |
| 6.1 Sol | 96.05 | 89.69 | 87.57 |
| 6 Sol | 86.46 | 88.82 | 87.41 |
| 6.1 Terra | 94.75 | 89.23 | 87.55 |
| 6 Luna | 80.74 | 87.50 | 85.79 |
| 5.6 Sol 请求 | 89.40 | 88.90 | 87.43 |

这些是各任务的自然质量指标，不是正确率、已知最优解百分比或IQ。每配置只有三个任务、每任务一次生成，不能把840个计划程序—输入组合当成840个独立模型样本。诊断修复未替换任何主分。

模型名称是请求标识，后端权重身份未核验；尤其5.6 Sol是接口接受的未文档化名称。Luna ultra不支持，未计零分。模型生成温度、随机种子和真实思考token不可见，同名思考档位不代表相同算力。工具禁用是共享工作区中的提示约束，并非硬隔离。

## 打开交互报告

完整解压ZIP，保持以下三个目录同级：

```text
model-comparison/
model-comparison-stress/
model-comparison-v3/
```

用浏览器打开 `model-comparison-v3/delivery/report.html`。点击矩阵格子即可查看原始源码、完整题包与逐输入结果；页面内可跳转前两轮报告。GitHub普通文件页面不会直接运行交互HTML。

报告中的“完整ZIP”链接指向其同目录文件。可直接使用本仓库上方下载链接；若希望该离线链接也可用，把下载的ZIP复制到解压后的 `model-comparison-v3/delivery/`。

## 核验与复算

ZIP SHA-256：

```text
75546e9d8e307b64191bd7dad27ccfabf76b082fda7a1c6211620b906c7a88a5
```

在仓库下载目录核验：

```bash
sha256sum -c archive.sha256
```

进入完整解压后的 `model-comparison-v3/`，用Python3.12运行：

```bash
python stage2/scripts/audit_results.py
python stage2/scripts/independent_review_audit.py
```

这些脚本从已保存输出复算，不重新执行限时程序。合法输出目标复算、原始文件哈希检查、独立审阅，以及迁移目录后禁止读取原工作区的解包重建检查均已通过。

## 题源与许可

完整包保留题源归属和许可文件：Frontier-CS固定commit `59687e5428266a22a49cf51f981b912103bfa91d`（GitHub仓库MIT）；ARC-AGI-2为Apache-2.0；BBEH材料为CC-BY-4.0、软件为Apache-2.0。各来源按原许可使用，本仓库不对全部第三方材料统一更换许可。公开题可能被模型训练见过；本实验不是官方完整排行榜。
