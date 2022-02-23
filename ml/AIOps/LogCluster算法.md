
# 1 介绍


# 2 相关工作
### SLCT

One of the earliest event log clustering algorithms is SLCT that is designed for mining line patterns and outlier events from textual event logs [2]. During the clustering process, SLCT assigns event log lines that fit the same pattern (e.g., Interface * down) to the same cluster, and all detected clusters are reported to the user as line patterns. For finding clusters in log data, the user has to supply the support threshold value s to SLCT which defines the minimum number of lines in each cluster. SLCT begins the clustering with a pass over the input data set, in order to identify frequent words which occur at least in s lines (word delimiter is customizable and defaults to whitespace). Also, each word is considered with its position in the line. For example, if s=2 and the data set contains the lines

最早的事件日志聚类算法之一是 SLCT，它设计用于从文本事件日志中挖掘行模式和异常事件 [2]。 在聚类过程中，SLCT 将符合相同模式（例如，Interface * down）的事件日志行分配给同一个类簇，并将所有检测到的类簇作为行模式报告给用户。 为了在日志数据中查找类簇，用户必须向 SLCT 提供支持阈值 s，SLCT 定义了每个类簇中的最小行数。 SLCT 通过对输入数据集的传递开始聚类，以识别至少在 s 行中出现的频繁单词（单词分隔符是可定制的，默认为空格）。 此外，每个单词都考虑其在行中的位置。 例如，如果 s=2 并且数据集包含行

Interface eth0 down
Interface eth1 down
Interface eth2 up


then words (Interface,1) and (down,3) occur in three and two lines, respectively, and are thus identified as frequent words. SLCT will then make another pass over the data set and create cluster candidates. When a line is processed during the data pass, all frequent words from the line are joined into a set which will act as a candidate for this line. After the data pass, candidates generated for at least s lines are reported as clusters together with their supports (occurrence times). Outliers are identified during an optional data pass and written to a user-specified file. For example, if s=2 then two cluster candidates {(Interface,1), (down,3)} and {(Interface,1)} are detected with supports 2 and 1, respectively. Thus, {(Interface,1), (down,3)} is the only cluster and is reported to the user as a line pattern Interface * down (since there is no word associated with the second position, an asterisk is printed for denoting a wildcard).Reported cluster covers the first two lines, while the line Interface eth2 up is considered an outlier.

（1）那么单词 (Interface,1) 和 (down,3) 分别出现在三行和两行中，因此被识别为频繁词。
（2）然后，SLCT 将再次遍历数据集并创建候选类簇。当在数据传递期间处理一行时，该行中的所有频繁词都被加入到一个集合中，该集合将作为该行的候选词。
（3）数据通过后，为至少 s 行生成的候选与它们的支持（出现次数）一起报告为类簇。在可选数据传递期间识别异常值并将其写入用户指定的文件。例如，如果 s=2，则检测到两个候选簇 {(Interface,1), (down,3)} 和 {(Interface,1)}，分别支持 2 和 1。因此，{(Interface,1), (down,3)} 是唯一的簇，并以行模式 Interface * down 的形式报告给用户（因为没有与第二个位置关联的单词，所以打印一个星号表示通配符）。报告的类簇覆盖了前两行，而 Interface eth2 up 行被认为是异常值。

SLCT has several shortcomings which have been pointed out in some recent works. Firstly, it is not able to detect wildcards after the last word in a line pattern [11]. For instance, if s=3 for three example lines above, the cluster {(Interface,1)} is reported to the user as a line pattern Interface, although most users would prefer the pattern Interface * *. Secondly, since word positions are encoded into words, the algorithm is sensitive to shifts in word positions and delimiter noise [8]. For instance, the line Interface HQ Link down would not be assigned to the cluster Interface * down, but would rather generate a separate cluster candidate. Finally, low support thresholds can lead to overfitting when larger clusters are split and resulting patterns are too specific [2].


SLCT 有几个缺点，在最近的一些工作中已经指出。 首先，它无法检测行模式中最后一个单词之后的通配符[11]。 例如，如果上面三个示例行的 s=3，集群 {(Interface,1)} 将作为行模式 Interface 报告给用户，尽管大多数用户更喜欢模板 Interface * *。 其次，由于单词位置被编码为单词，因此该算法对单词位置的变化和分隔符噪声很敏感[8]。 例如，Line Interface HQ Link down 不会分配给类簇 Interface * down，而是生成一个单独的类簇候选。 最后，当更大的集群被分割并且结果模式过于具体时，低支持阈值会导致过度拟合[2]。

自动日志解析，分配符合**相同模式**的事件日志行到相同簇中，所有检测的簇都被作为行模式。用户需要提供支持阈值 s 以便SLCT定义每个簇中**最少行数量**。在日志处理期间，所有来自日志的频繁词放入集合作为此日志的候选。

1. 建立单词字典，对所有日志建立包含单词频率和坐标的字典；
2. 建立日志簇；
3. 生成日志模板。

Reidemeister, Jiang, Munawar and Ward [6, 7, 8] developed a methodology that addresses some of the above shortcomings. The methodology uses event log mining techniques for diagnosing recurrent faults in software systems. First, a modified version of SLCT is used for mining line patterns from labeled event logs. In order to handle clustering errors caused by shifts in word positions and delimiter noise, line patterns from SLCT are clustered with a single-linkage clustering algorithm which employs a variant of the Levenshtein distance function. After that, a common line pattern description is established for each cluster of line patterns. According to [8], single-linkage clustering and post-processing its results add minimal runtime overhead to the clustering by SLCT. The final results are converted into bit vectors and used for building decision-tree classifiers, in order to identify recurrent faults in future event logs.


Reidemeister、Jiang、Munawar 和 Ward [6, 7, 8] 开发了一种方法来解决上述一些缺点。 该方法使用事件日志挖掘技术来诊断软件系统中的经常性故障。 首先，SLCT 的修改版本用于从标记的事件日志中挖掘行模式。 为了处理由单词位置偏移和分隔符噪声引起的聚类错误，来自 SLCT 的线条模式使用单链接聚类算法进行聚类，该算法采用 Levenshtein 距离函数的变体。 之后，为每个线型集群建立一个共同的线型描述。 根据[8]，单链接聚类和后处理其结果为 SLCT 的聚类增加了最小的运行时开销。 最终结果被转换为位向量并用于构建决策树分类器，以识别未来事件日志中的重复故障。

Another clustering algorithm that mines line patterns from event logs is IPLoM by Makanju, Zincir-Heywood and Milios [10, 11]. Unlike SLCT, IPLoM is a hierarchical clustering algorithm which starts with the entire event log as a single partition, and splits partitions iteratively during three steps. Like SLCT, IPLoM considers words with their positions in event log lines, and is therefore sensitive to shifts in word positions. During the first step, the initial partition is split by assigning lines with the same number of words to the same partition. During the second step, each partition is divided further by identifying the word position with the least number of unique words, and splitting the partition by assigning lines with the same word to the same partition. During the third step, partitions are split based on associations between word pairs. At the final stage of the algorithm, a line pattern is derived for each partition. Due to its hierarchical nature, IPLoM does not need the support threshold, but takes several other parameters (such as partition support threshold and cluster goodness threshold) which impose fine-grained control over splitting of partitions [11]. As argued in [11], one advantage of IPLoM over SLCT is its ability to detect line patterns with wildcard tails (e.g., Interface * *), and the author has reported higher precision and recall for IPLoM.

另一种从事件日志中挖掘线型的聚类算法是 Makanju、Zincir-Heywood 和 Milios [10, 11] 的 IPLoM。与 SLCT 不同，IPLoM 是一种层次聚类算法，它从整个事件日志作为单个分区开始，并在三个步骤中迭代地拆分分区。与 SLCT 一样，IPLoM 考虑单词及其在事件日志行中的位置，因此对单词位置的变化很敏感。在第一步中，通过将具有相同字数的行分配给同一分区来拆分初始分区。在第二步中，通过识别具有最少唯一词数的词位置来进一步划分每个分区，并通过将具有相同单词的行分配给同一分区来划分分区。在第三步中，根据词对之间的关​​联划分分区。在算法的最后阶段，为每个分区导出一个线型。由于其分层性质，IPLoM 不需要支持阈值，而是采用其他几个参数（例如分区支持阈值和集群良好度阈值），这些参数对分区的拆分进行了细粒度控制 [11]。正如 [11] 中所述，IPLoM 优于 SLCT 的一个优势是它能够检测带有通配符尾部的线条模式（例如，接口 * *），并且作者报告了 IPLoM 的更高精度和召回率。


# 3 LogCluster 算法
$L = [l_1, l_2, ..., l_n]$是文本事件日志，由 n 行组成，每行 $l_i (1<=i<=n)$ 是事件的完全表征，i 是行唯一标识；

每行 $l_i$ 是 k 个词的序列，$l_i = (w_{i,1}, w_{i,2}, ..., w_{i,k_i})$。

LogCluster 使用支持阈值 $s(1<=s<=n)$ 作为输入参数，将日志划分到 $C_1, C_2, ..., C_m$ 簇中，每簇至少 s 条日志，O是离群簇。

Log Cluster 将日志聚类问题视作模式挖掘问题，每簇 $C_j$ 通过模式 $p_j$ 标识为唯一的，类簇内所有行与之匹配。为检测簇，Log Cluster 从日志中挖掘模式 $p_j$。模式 $p_j$ 和簇 $C_j$ 的支持值定义为 $C_j$ 中日志的数量，每种模式由词（wrods）和通配符（wildcards）组成。例如：通配符$*\{1, 3\}$ 表示匹配1到3个单词。


## 构建频繁词
为找到达到支持阈值的模式，每种模式的所有词至少要发生在 s 条事件日志中。

Log Cluster 考虑日志中的每个词但是**不包括位置信息**。$I_w$ 是包含单词 w 的行标识的集合。如果 $I_w$ 大于等于阈值 s ，则 w 是频繁词，所有频繁词的集合使用 F 表示。

Log Cluster 使用一个 h 大小的框架计数器。在预先处理事件日志时，每条事件日志行的去重词散列到 0 到 h-1的整数，增加对应的计数数量。(构建词表，统计词频)。

设想的实现方式：每行日志分词后，词汇去重，统计所有词汇的词频，超过阈值 s 的为频繁词

## 生成候选簇
频繁词集合构建后，LogCluster 产生簇的候选。
对事件日志中的每行，LogCluster 从日志提取所有频繁词，将词处理为元组，保留原始行中原始位置，元组会作为候选簇的标识，所在行会被归为对应的候选。

如果给定的候选不存在，则初始化并将支持计数设为1，从行中创建其行模式。如果候选存在，其支持计数增加，行模式调整以覆盖当前行。

Log Cluster不记录分配给候选簇的日志。

举例：事件日志“Interface DMZ-link down at node router2”，频繁词是“Interface, down, at, node”，该行被分配给识别的候选元组(Interface, down, at, node)。如果候选不存在，则设置行模式初始化为“Interface *{1,1} down at node *{1,1}”，计数设为 1，通配符 *{1，1}可匹配任何单一词汇。如果下一行产生同样的候选标识“Interface HQ link down at node router2”，候选支持计数增加到 2。行模式设置为“Interface *{1,2} down at node *{1,1}”，为使模式匹配，至少一个但不超过2个在 interface和down之间。

设想的实现方式：根据每条日志中的频繁词(保持其原有词序)，将有相同频繁词的日志归并，并提取对应的模式，提取后模式数量小于 s 的模式删除，之后即可获得模式提取结果。



# 参考资料

[Log Cluster：日志数据聚类和模式挖掘算法](https://blog.csdn.net/MarkAustralia/article/details/122242966)



