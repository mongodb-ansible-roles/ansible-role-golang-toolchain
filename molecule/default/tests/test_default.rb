# frozen_string_literal: true

describe directory('/opt/golang') do
  it { should exist }
end

describe command('GOROOT=/opt/golang/go1.7 /opt/golang/go1.7/bin/go version') do
  its('stdout') { should eq "go version go1.7.6 linux/amd64\n" }
end

describe command('GOROOT=/opt/golang/go1.8 /opt/golang/go1.8/bin/go version') do
  its('stdout') { should eq "go version go1.8.7 linux/amd64\n" }
end

describe command('GOROOT=/opt/golang/go1.9 /opt/golang/go1.9/bin/go version') do
  its('stdout') { should eq "go version go1.9.7 linux/amd64\n" }
end

describe command('GOROOT=/opt/golang/go1.10 /opt/golang/go1.10/bin/go version') do
  its('stdout') { should eq "go version go1.10.8 linux/amd64\n" }
end

describe command('GOROOT=/opt/golang/go1.11 /opt/golang/go1.11/bin/go version') do
  its('stdout') { should eq "go version go1.11.9 linux/amd64\n" }
end

describe command('GOROOT=/opt/golang/go1.12 /opt/golang/go1.12/bin/go version') do
  its('stdout') { should eq "go version go1.12.8 linux/amd64\n" }
end
