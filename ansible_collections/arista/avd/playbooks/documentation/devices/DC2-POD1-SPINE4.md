# DC2-POD1-SPINE4
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.65.13/24 | 10.6.65.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 10.6.65.13/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---- | ----- |
| False | True |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$82gqIqw8b3nibNrk$MoZO0S8QMQN8uwnR8v48dbGrL0Ec/6q36tSx8y9IsExi4L.HtmokW9rX8VehLxhg542mNTBKqxMBF.LgnCTm4.
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | AMS DC2 DC2_POD1 DC2-POD1-SPINE4 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC2 DC2_POD1 DC2-POD1-SPINE4
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet32/1 | routed | - | 172.17.64.158/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC2-POD1-LEAF1B_Ethernet32/1 | routed | - | 172.17.64.166/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC2-POD1-LEAF2A_Ethernet32/1 | routed | - | 172.17.64.182/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC2-POD1-LEAF2B_Ethernet32/1 | routed | - | 172.17.64.190/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC2-POD1-LEAF3A_Ethernet32/1 | routed | - | 172.17.64.198/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC2-POD1-LEAF3B_Ethernet32/1 | routed | - | 172.17.64.206/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC2-POD1-LEAF4A_Ethernet32/1 | routed | - | 172.17.64.214/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC2-POD1-LEAF4B_Ethernet32/1 | routed | - | 172.17.64.222/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC2-POD1-LEAF5A_Ethernet32/1 | routed | - | 172.17.64.230/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC2-POD1-LEAF5B_Ethernet32/1 | routed | - | 172.17.64.238/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC2-POD1-LEAF6A_Ethernet32/1 | routed | - | 172.17.64.246/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC2-POD1-LEAF6B_Ethernet32/1 | routed | - | 172.17.64.254/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC2-POD1-LEAF7A_Ethernet32/1 | routed | - | 172.17.65.6/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC2-POD1-LEAF7B_Ethernet32/1 | routed | - | 172.17.65.14/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC2-POD1-LEAF8A_Ethernet32/1 | routed | - | 172.17.65.22/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC2-POD1-LEAF8B_Ethernet32/1 | routed | - | 172.17.65.30/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC2-POD1-LEAF9A_Ethernet32/1 | routed | - | 172.17.65.38/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC2-POD1-LEAF9B_Ethernet32/1 | routed | - | 172.17.65.46/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC2-POD1-LEAF10A_Ethernet32/1 | routed | - | 172.17.65.54/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC2-POD1-LEAF10B_Ethernet32/1 | routed | - | 172.17.65.62/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC2-POD1-LEAF11A_Ethernet32/1 | routed | - | 172.17.65.70/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC2-POD1-LEAF11B_Ethernet32/1 | routed | - | 172.17.65.78/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC2-POD1-LEAF12A_Ethernet32/1 | routed | - | 172.17.65.86/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC2-POD1-LEAF12B_Ethernet32/1 | routed | - | 172.17.65.94/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC2-POD1-LEAF13A_Ethernet32/1 | routed | - | 172.17.65.102/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC2-POD1-LEAF13B_Ethernet32/1 | routed | - | 172.17.65.110/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC2-POD1-LEAF14A_Ethernet32/1 | routed | - | 172.17.65.118/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC2-POD1-LEAF14B_Ethernet32/1 | routed | - | 172.17.65.126/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet12/1 | routed | - | 172.16.64.27/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet12/1 | routed | - | 172.16.64.91/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet12/1 | routed | - | 172.16.64.155/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet12/1 | routed | - | 172.16.64.219/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.158/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC2-POD1-LEAF1B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.166/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC2-POD1-LEAF2A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.182/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC2-POD1-LEAF2B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.190/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC2-POD1-LEAF3A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.198/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC2-POD1-LEAF3B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.206/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC2-POD1-LEAF4A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.214/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC2-POD1-LEAF4B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.222/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC2-POD1-LEAF5A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.230/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC2-POD1-LEAF5B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.238/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC2-POD1-LEAF6A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.246/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC2-POD1-LEAF6B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.254/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC2-POD1-LEAF7A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.6/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC2-POD1-LEAF7B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.14/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC2-POD1-LEAF8A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.22/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC2-POD1-LEAF8B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.30/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC2-POD1-LEAF9A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.38/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC2-POD1-LEAF9B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.46/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC2-POD1-LEAF10A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.54/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC2-POD1-LEAF10B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.62/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC2-POD1-LEAF11A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.70/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC2-POD1-LEAF11B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.78/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC2-POD1-LEAF12A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.86/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC2-POD1-LEAF12B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.94/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC2-POD1-LEAF13A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.102/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC2-POD1-LEAF13B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.110/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC2-POD1-LEAF14A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.118/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC2-POD1-LEAF14B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.126/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet12/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.27/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet12/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.91/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet12/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.155/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet12/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.219/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.64.14/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.64.14/32
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| mgmt | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.65.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.65.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 64804|  10.4.64.14 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- |
| 172.16.64.26 | 64501 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.64.90 | 64502 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.64.154 | 64503 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.64.218 | 64504 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.159 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.167 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.183 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.191 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.199 | 65103 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.207 | 65103 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.215 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.223 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.231 | 65105 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.239 | 65105 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.247 | 65106 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.255 | 65106 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.7 | 65107 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.15 | 65107 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.23 | 65108 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.31 | 65108 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.39 | 65109 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.47 | 65109 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.55 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.63 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.71 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.79 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.87 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.95 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.103 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.111 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.119 | 65114 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.127 | 65114 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 64804
   router-id 10.4.64.14
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.64.26 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.26 remote-as 64501
   neighbor 172.16.64.26 description SUPER-SPINE1_Ethernet12/1
   neighbor 172.16.64.90 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.90 remote-as 64502
   neighbor 172.16.64.90 description SUPER-SPINE2_Ethernet12/1
   neighbor 172.16.64.154 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.154 remote-as 64503
   neighbor 172.16.64.154 description SUPER-SPINE3_Ethernet12/1
   neighbor 172.16.64.218 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.218 remote-as 64504
   neighbor 172.16.64.218 description SUPER-SPINE4_Ethernet12/1
   neighbor 172.17.64.159 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.159 remote-as 65101
   neighbor 172.17.64.159 description DC2-POD1-LEAF1A_Ethernet32/1
   neighbor 172.17.64.167 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.167 remote-as 65101
   neighbor 172.17.64.167 description DC2-POD1-LEAF1B_Ethernet32/1
   neighbor 172.17.64.183 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.183 remote-as 65102
   neighbor 172.17.64.183 description DC2-POD1-LEAF2A_Ethernet32/1
   neighbor 172.17.64.191 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.191 remote-as 65102
   neighbor 172.17.64.191 description DC2-POD1-LEAF2B_Ethernet32/1
   neighbor 172.17.64.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.199 remote-as 65103
   neighbor 172.17.64.199 description DC2-POD1-LEAF3A_Ethernet32/1
   neighbor 172.17.64.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.207 remote-as 65103
   neighbor 172.17.64.207 description DC2-POD1-LEAF3B_Ethernet32/1
   neighbor 172.17.64.215 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.215 remote-as 65104
   neighbor 172.17.64.215 description DC2-POD1-LEAF4A_Ethernet32/1
   neighbor 172.17.64.223 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.223 remote-as 65104
   neighbor 172.17.64.223 description DC2-POD1-LEAF4B_Ethernet32/1
   neighbor 172.17.64.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.231 remote-as 65105
   neighbor 172.17.64.231 description DC2-POD1-LEAF5A_Ethernet32/1
   neighbor 172.17.64.239 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.239 remote-as 65105
   neighbor 172.17.64.239 description DC2-POD1-LEAF5B_Ethernet32/1
   neighbor 172.17.64.247 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.247 remote-as 65106
   neighbor 172.17.64.247 description DC2-POD1-LEAF6A_Ethernet32/1
   neighbor 172.17.64.255 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.255 remote-as 65106
   neighbor 172.17.64.255 description DC2-POD1-LEAF6B_Ethernet32/1
   neighbor 172.17.65.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.7 remote-as 65107
   neighbor 172.17.65.7 description DC2-POD1-LEAF7A_Ethernet32/1
   neighbor 172.17.65.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.15 remote-as 65107
   neighbor 172.17.65.15 description DC2-POD1-LEAF7B_Ethernet32/1
   neighbor 172.17.65.23 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.23 remote-as 65108
   neighbor 172.17.65.23 description DC2-POD1-LEAF8A_Ethernet32/1
   neighbor 172.17.65.31 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.31 remote-as 65108
   neighbor 172.17.65.31 description DC2-POD1-LEAF8B_Ethernet32/1
   neighbor 172.17.65.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.39 remote-as 65109
   neighbor 172.17.65.39 description DC2-POD1-LEAF9A_Ethernet32/1
   neighbor 172.17.65.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.47 remote-as 65109
   neighbor 172.17.65.47 description DC2-POD1-LEAF9B_Ethernet32/1
   neighbor 172.17.65.55 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.55 remote-as 65110
   neighbor 172.17.65.55 description DC2-POD1-LEAF10A_Ethernet32/1
   neighbor 172.17.65.63 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.63 remote-as 65110
   neighbor 172.17.65.63 description DC2-POD1-LEAF10B_Ethernet32/1
   neighbor 172.17.65.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.71 remote-as 65111
   neighbor 172.17.65.71 description DC2-POD1-LEAF11A_Ethernet32/1
   neighbor 172.17.65.79 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.79 remote-as 65111
   neighbor 172.17.65.79 description DC2-POD1-LEAF11B_Ethernet32/1
   neighbor 172.17.65.87 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.87 remote-as 65112
   neighbor 172.17.65.87 description DC2-POD1-LEAF12A_Ethernet32/1
   neighbor 172.17.65.95 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.95 remote-as 65112
   neighbor 172.17.65.95 description DC2-POD1-LEAF12B_Ethernet32/1
   neighbor 172.17.65.103 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.103 remote-as 65113
   neighbor 172.17.65.103 description DC2-POD1-LEAF13A_Ethernet32/1
   neighbor 172.17.65.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.111 remote-as 65113
   neighbor 172.17.65.111 description DC2-POD1-LEAF13B_Ethernet32/1
   neighbor 172.17.65.119 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.119 remote-as 65114
   neighbor 172.17.65.119 description DC2-POD1-LEAF14A_Ethernet32/1
   neighbor 172.17.65.127 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.127 remote-as 65114
   neighbor 172.17.65.127 description DC2-POD1-LEAF14B_Ethernet32/1
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

# Multicast

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.64.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.64.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB in AMS.yml

```
