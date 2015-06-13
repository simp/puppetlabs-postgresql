require 'spec_helper'

describe 'postgresql::repo', :type => :class do
  let :facts do
    {
      :osfamily               => 'RedHat',
      :operatingsystem        => 'RedHat',
      :operatingsystemrelease => '7.0',
      :lsbdistid              => 'RedHatEnterpriseServer',
      :lsbdistcodename        => 'Maipo',
    }
  end

  let :params do
    {
      :version => '5'
    }
  end

  describe 'with no parameters' do
    it 'should instantiate yum_postgresql_org class' do
      is_expected.to contain_class('postgresql::repo::yum_postgresql_org')
    end
  end
end
