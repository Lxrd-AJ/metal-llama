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
    - [ ] torch dataset class to load 
        - [x] tiny shakespeare
        - [ ] FineWeb EDU
    - [ ] Llama BPE tokeniser
    - [ ] Cache encodings: Save the processed tokenised string as `uint16` and use that instead of encoding on the fly. If there is no cache, create it and save it for next time.
    - [ ] Use memory mapped files (numpy.memmap) to reach the cached encodings so that I don't have to load them all into RAM
- Model Architecture
    - [ ] Llama architecture
    - [ ] load the existing Llama 2 weights https://huggingface.co/meta-llama/Llama-2-7b
- Training loop
    - [ ] Initial small & simple training loop
    - [ ] Evaluate the model perplexity - $exp(H(p))$ where $H(p)$ is the cross-entropy loss on a validation set
- Apple Silicon optim
    - [ ] To CoreML or MLX (Swift), tis the question?
- Efficient ML
    - [ ] Implement a KV-cache
    - [ ] Int8 quantisation
- PyTorch & Apple Silicon profiling
- [ ] Measure memory and latency
    - [ ] Time to first token
    - [ ] Time per output token
    - [ ] KV Cache size and growth as context window fills up
- [ ] Use `torch.profiler` and Apple tools to profile
    - [ ] PyTorch
        - [ ] BF16 model version
        - [ ] Int8 Quant version
    - [ ] CoreML/MLX
        - [ ] BF16 model version
        - [ ] Int8 Quant version