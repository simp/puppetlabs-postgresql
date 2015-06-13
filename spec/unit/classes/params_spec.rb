require 'spec_helper'

describe 'postgresql::params', :type => :class do
  let :facts do
    {
      :osfamily               => 'RedHat',
      :operatingsystem        => 'RedHat',
      :operatingsystemrelease => '7.0',
      :lsbdistid              => 'RedHatEnterpriseServer',
      :lsbdistcodename        => 'Maipo',
    }
  end

  it { is_expected.to contain_class("postgresql::params") }
end
