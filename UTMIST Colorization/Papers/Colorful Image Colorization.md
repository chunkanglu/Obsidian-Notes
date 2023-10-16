- Guessing plausible colors based on semantic context
- Uses CIE $Lab$ colorspace which separates luminance (value) from the color
- Previous works desaturated
	- loss function encourage conservative predictions minimizing euclidean error
- Introduce multimodel prediction of distribution of possible colors for each pixel
	- emphasise rare colors
	- Annealed-mean of distribution
- Tested with colorization Turing test with humans
- self supervised representation learning
![[Pasted image 20231015110947.png]]

# Approach
- Distances in CIE $Lab$ color space model perceptual distance, how different human eyes preceive it
- Multinomial classification
- Quantize $ab$ output space with grid size 10 (total 313 $ab$ pairs)
- For given input, predict probability of possible color bin
	- Comparing pred to truth, for truth color $Y$, find 5 nearest neighbour to $Y$ in output space and weigh proportionally from ground truth
	- Then multinomial cross entropy loss
		- Includes rebalance term based on color-class rarity
## Class rebalancing
- $ab$ values strongly biased towards lower values due to backgrounds like clouds, pavement, dirt, walls
	- much more desaturated values
	- loss function dominated by desaturated values
- Each pixel reweighted at train time based on closest $ab$ bin
- For smooth color distribution, used Gaussian kernel mixed with uniform distrubution

## Predicting Color
- Define function $H$ mapping predicted distribution to $ab$ point estimate
- Taking mode of distribution creates vibrant but not spatially consistent color
- Taking mean creates desaturated colors
- **Annealed-mean:** Interpolate by re-adjusting temperature $T$ of softmax distribution then taking mean of result
	- Lowering $T$ towards 0 gets it closer to mode, increasing vibrancy
	- Increasing $T$ towards 1 gets it closer to mean, to maintain spatial coherence
	- $T = 0.38$ in paper
- $H$ operates on each pixel independently, can be part of feed forward pass of CNN

## Evaluating Quality of Color
### Perceptual realism
- Human participants guess if photo contained fake colors
- Fooled participant on 32% of trials
### Semantic interpretability (VGG classification)
- Can it be interpretable to off the shelf object classifier
	- feed fake colorized images to a VGG network
### Raw accuracy
> As a low-level test, we compute the percentage of predicted pixel colors within a thresholded L2 distance of the ground truth in ab color space. We then sweep across thresholds from 0 to 150 to produce a cumulative mass function, as introduced in [22], integrate the area under the curve (AuC), and normalize. Note that this AuC metric measures raw prediction accuracy, whereas our method aims for plausibility.
- Even predicting gray for every pixel does well and full method with class rebalancing achieves approximately same score
- Re-weight pixels inversely by color class probability and check in regions with higher saturation
## Self Supervised Feature Learning
### Cross Channel Encoding
