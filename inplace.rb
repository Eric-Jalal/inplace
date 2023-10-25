class Inplace < Formula
  desc "A command-line tool to find and replace text in files"
  homepage "https://github.com/Eric-Jalal/eric-tools-repelit"
  url "https://github.com/Eric-Jalal/inplace/archive/refs/tags/v1.0.0.tar.gz"
  name "inplace"
  sha256 "7a822ac0ff2abd28144327d077f736a82e6c2165d4bbee54d0f0773f4445017b"
  version "1.0.0"
  license "MIT"

  def install
    bin.install "inplace.py" => "inplace"
  end

  test do
    system "#{bin}/inplace", "--version"
  end
end

