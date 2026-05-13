# Metal Llama

Metal Llama is a from-scratch implementation of the Llama 2 architecture, designed specifically to bridge the gap between high-level research and hardware-aware deployment. 

## 🛠 Features
* Llama 2 architecture: A ground-up implementation of Llama 2 including:
    * RoPE (Rotary Positional Embeddings): For better context scaling.
    * RMSNorm: For improved training stability.
    * SwiGLU Activations: For enhanced representation capacity.
    
* Dual-Framework Pipeline:
    * Training: PyTorch-based training loop optimized for $BF16$.
    * Inference: Native Swift implementation using the MLX framework for zero-overhead execution on Apple's Unified Memory.

* Embedded Optimization: 
    * Custom INT8 Symmetric (Absmax) Quantization implemented from scratch.
    * Benchmarking suite for TTFT (Time to First Token) and TPOT (Time per Output Token).

# TODOs:
- Datasets
    - [x] TinyShakespeare data and Character level tokeniser
    - [ ] torch dataset class to load either tiny shakespeare or FineWeb EDU
    - [ ] Llama BPE tokeniser
    - [ ] Cache encodings: Save the processed tokenised string as `uint16` and use that instead of encoding on the fly
    - [ ] Use memory mapped files to reach the cached encodings so that I don't have to load them all into RAM