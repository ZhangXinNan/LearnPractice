

Distilling the Knowledge in a Neural Network

Geoffrey Hinton∗†
Google Inc.
Mountain View
geoffhinton@google.com

Oriol Vinyals†
Google Inc.
Mountain View
vinyals@google.com

Jeff Dean
Google Inc.
Mountain View
jeff@google.com


# 1 Introduction
Many insects have a larval form that is optimized for extracting energy and nutrients from the environment
and a completely different adult form that is optimized for the very different requirements
of traveling and reproduction. In large-scale machine learning, we typically use very similar models
for the training stage and the deployment stage despite their very different requirements: For tasks
like speech and object recognition, training must extract structure from very large, highly redundant
datasets but it does not need to operate in real time and it can use a huge amount of computation.
Deployment to a large number of users, however, has much more stringent requirements on latency
and computational resources. The analogy with insects suggests that we should be willing to train
very cumbersome models if that makes it easier to extract structure from the data. The cumbersome
model could be an ensemble of separately trained models or a single very large model trained with
a very strong regularizer such as dropout [9]. Once the cumbersome model has been trained, we
can then use a different kind of training, which we call “distillation” to transfer the knowledge from
the cumbersome model to a small model that is more suitable for deployment. A version of this
strategy has already been pioneered by Rich Caruana and his collaborators [1]. In their important
paper they demonstrate convincingly that the knowledge acquired by a large ensemble of models
can be transferred to a single small model.

许多昆虫的幼虫形态经过优化，可以从环境中获取能量和营养，而成虫形态则完全不同，以满足迁徙和繁殖等截然不同的需求。在大规模机器学习中，我们通常在训练阶段和部署阶段使用非常相似的模型，尽管它们的需求截然不同：对于语音和物体识别等任务，训练必须从非常庞大、高度冗余的数据集中提取结构，但它不需要实时运行，并且可能使用大量计算。然而，部署到大量用户对延迟和计算资源的要求要严格得多。与昆虫的类比表明，如果训练非常繁琐的模型更容易从数据中提取结构，我们应该愿意训练它。繁琐的模型可以是多个单独训练的模型的集合，也可以是一个使用非常强的正则化器（例如dropout [9]）训练的单个非常大的模型。一旦庞大的模型训练完毕，我们就可以采用另一种训练方法，我们称之为“蒸馏”，将知识从庞大的模型迁移到更适合部署的小型模型。Rich Caruana 及其同事 [1] 已经率先提出了这种策略的一个版本。在他们重要的论文中，他们令人信服地证明了，大量模型所获得的知识可以迁移到单个小型模型中。



A conceptual block that may have prevented more investigation of this very promising approach is
that we tend to identify the knowledge in a trained model with the learned parameter values and this
makes it hard to see how we can change the form of themodel but keep the same knowledge. A more
abstract view of the knowledge, that frees it from any particular instantiation, is that it is a learned
mapping from input vectors to output vectors. For cumbersome models that learn to discriminate
between a large number of classes, the normal training objective is to maximize the average log
probability of the correct answer, but a side-effect of the learning is that the trained model assigns
probabilities to all of the incorrect answers and even when these probabilities are very small, some
of them are much larger than others. The relative probabilities of incorrect answers tell us a lot about
how the cumbersome model tends to generalize. An image of a BMW, for example, may only have
a very small chance of being mistaken for a garbage truck, but that mistake is still many times more
probable than mistaking it for a carrot.

一个概念上的障碍可能阻碍了对这一极具前景的方法进行进一步的研究，那就是：我们倾向于将训练模型中的知识与学习到的参数值等同起来，这使得我们很难理解如何在保持知识不变的情况下改变模型的形式。一种更抽象的观点，将知识从任何特定的实例中解放出来，认为它是从输入向量到输出向量的学习映射。对于学习区分大量类别的繁琐模型来说，正常的训练目标是最大化正确答案的平均对数概率，但这种学习的一个副作用是，训练后的模型会为所有错误答案分配概率，即使这些概率非常小，其中一些概率也比其他概率大得多。错误答案的相对概率可以告诉我们很多关于繁琐模型如何泛化的信息。例如，一张宝马的图片被误认为是垃圾车的概率非常小，但这种错误仍然比被误认为是胡萝卜的概率高出许多倍。

It is generally accepted that the objective function used for training should reflect the true objective
of the user as closely as possible. Despite this, models are usually trained to optimize performance
on the training data when the real objective is to generalize well to new data. It would clearly
be better to train models to generalize well, but this requires information about the correct way to
generalize and this information is not normally available. When we are distilling the knowledge
from a large model into a small one, however, we can train the small model to generalize in the same
way as the large model. If the cumbersome model generalizes well because, for example, it is the
average of a large ensemble of differentmodels, a small model trained to generalize in the same way
will typically do much better on test data than a small model that is trained in the normal way on the
same training set as was used to train the ensemble.

人们普遍认为，用于训练的目标函数应该尽可能真实地反映用户的真实目标。尽管如此，模型的训练目标通常是优化在训练数据上的性能，而其真正的目标是在新数据上实现良好的泛化。训练模型使其具有良好的泛化能力显然更好，但这需要关于正确泛化方式的信息，而这些信息通常难以获得。然而，当我们将知识从大型模型提炼到小型模型时，我们可以训练小型模型以与大型模型相同的方式进行泛化。如果大型模型泛化良好，例如，它是大量不同模型的平均值，那么以相同方式训练的小型模型在测试数据上的表现通常会比在用于训练集成的相同训练集上以常规方式训练的小型模型好得多。

An obvious way to transfer the generalization ability of the cumbersome model to a small model is
to use the class probabilities produced by the cumbersome model as “soft targets” for training the
small model. For this transfer stage, we could use the same training set or a separate “transfer” set.
When the cumbersome model is a large ensemble of simpler models, we can use an arithmetic or
geometric mean of their individual predictive distributions as the soft targets. When the soft targets
have high entropy, they providemuch more information per training case than hard targets and much
less variance in the gradient between training cases, so the small model can often be trained on much
less data than the original cumbersome model and using a much higher learning rate.

将复杂模型的泛化能力迁移到小型模型的一个显而易见的方法是，
使用复杂模型生成的类别概率作为训练小型模型的“软目标”。在这个迁移阶段，我们可以使用相同的训练集，也可以使用单独的“迁移”集。
当复杂模型是由多个简单模型组成的大型集合时，我们可以将它们各自预测分布的算术平均值或几何平均值用作软目标。当软目标具有高熵时，它们在每个训练案例中提供的信息量远高于硬目标，并且训练案例之间的梯度方差也远小于硬目标，因此，小型模型通常可以在比原始复杂模型少得多的数据量上进行训练，并使用更高的学习率。

For tasks like MNIST in which the cumbersome model almost always produces the correct answer
with very high confidence, much of the information about the learned function resides in the ratios
of very small probabilities in the soft targets. For example, one version of a 2 may be given a
probability of $10^{−6}$ of being a 3 and $10^{−9}$ of being a 7 whereas for another version it may be the
other way around. This is valuable information that defines a rich similarity structure over the data
(i. e. it says which 2’s look like 3’s and which look like 7’s) but it has very little influence on the
cross-entropy cost function during the transfer stage because the probabilities are so close to zero.
Caruana and his collaborators circumvent this problem by using the logits (the inputs to the final
softmax) rather than the probabilities produced by the softmax as the targets for learning the small
model and they minimize the squared difference between the logits produced by the cumbersome
model and the logits produced by the small model. Our more general solution, called “distillation”,
is to raise the temperature of the final softmax until the cumbersome model produces a suitably soft
set of targets. We then use the same high temperature when training the small model to match these
soft targets. We show later that matching the logits of the cumbersome model is actually a special
case of distillation.

对于像 MNIST 这样的任务，繁琐的模型几乎总能以极高的置信度得出正确答案，而学习函数的大部分信息都存在于软目标中非常小的概率之比中。例如，一个数字 2 的版本可能被赋予 $10^{−6}$ 的概率表示为 3，$10^{−9}$ 的概率表示为 7，而另一个版本则可能正好相反。这些信息非常有价值，它定义了数据中丰富的相似性结构（例如，它表明哪些 2 看起来像 3，哪些看起来像 7），但在迁移阶段，它对交叉熵成本函数的影响非常小，因为概率非常接近于零。
Caruana 和他的同事们规避了这个问题，他们使用 logits（最终 softmax 的输入）而不是 softmax 产生的概率作为学习小模型的目标，并最小化了繁琐模型产生的 logits 与小模型产生的 logits 之间的平方差。我们更通用的解决方案，称为“蒸馏”，是提高最终 softmax 的温度，直到繁琐模型产生一组足够柔软的目标。然后，我们在训练小模型时使用相同的高温来匹配这些柔软的目标。我们稍后会证明，匹配繁琐模型的 logits 实际上是蒸馏的一个特例。

The transfer set that is used to train the small model could consist entirely of unlabeled data [1]
or we could use the original training set. We have found that using the original training set works
well, especially if we add a small term to the objective function that encourages the small model
to predict the true targets as well as matching the soft targets provided by the cumbersome model.
Typically, the small model cannot exactly match the soft targets and erring in the direction of the
correct answer turns out to be helpful.

用于训练小型模型的迁移集可以完全由未标记数据 [1] 组成，或者我们可以使用原始训练集。我们发现使用原始训练集效果很好，尤其是在目标函数中添加一个小项，鼓励小型模型预测真实目标，并匹配大型模型提供的软目标的情况下。
通常情况下，小型模型无法完全匹配软目标，因此，朝着正确答案的方向进行调整会有所帮助。



