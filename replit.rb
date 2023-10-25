class FindReplace < Formula
  desc "A command-line tool to find and replace text in files"
  homepage "https://github.com/Eric-Jalal/eric-tools-repelit"
  url "https://github.com/Eric-Jalal/eric-tools-repelit/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "fe272dd54f435468a534c180eb85b16a29bae42ab0c46aa2f4258c8f0c852433"
  version "1.0.0"
  license "MIT"

  def install
    bin.install "repelit.py" => "repelit"
  end

  test do
    system "#{bin}/repelit", "--version"
  end
end

