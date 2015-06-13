require 'spec_helper'

describe 'postgresql::globals', :type => :class do
  let :facts do
    {
      :osfamily               => 'RedHat',
      :operatingsystem        => 'RedHat',
      :operatingsystemrelease => '7.0',
      :lsbdistid              => 'RedHatEnterpriseServer',
      :lsbdistcodename        => 'Maipo',
    }
  end

  describe 'with no parameters' do
    it 'should work' do
      is_expected.to contain_class("postgresql::globals")
    end
  end

  describe 'manage_package_repo => true' do
    let(:params) do
      {
        :manage_package_repo => true,
      }
    end
    it 'should pull in class postgresql::repo' do
      is_expected.to contain_class("postgresql::repo")
    end
  end
end
